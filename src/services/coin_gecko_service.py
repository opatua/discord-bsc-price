import time
from typing import Any, Dict

from django.conf import settings
from django.core.cache import cache

from src.services.date_service import DateService
from src.services.third_party_service import ThirdPartyService


class CoinGeckoService:
    date_service = DateService()
    third_party_service = ThirdPartyService()
    coin_gecko_cache_key = 'coin_gecko'

    def get_details_by_contract(
        self,
        contract_address: str,
        network: str,
    ):
        coin_gecko_response = cache.get(
            f'{self.coin_gecko_cache_key}_{network}_{contract_address}',
        )
        if coin_gecko_response:
            return coin_gecko_response

        coin_gecko_response = {}
        try:
            coin_gecko_response = self.third_party_service.call(
                'GET',
                f'{settings.COIN_GECKO_URL}/coins/{network}/contract/{contract_address}',
                None,
            ).json()
        except:
            time.sleep(settings.DISCORD_BOT_FETCH_INTERVAL)
            print(
                f"Retry calling coingecko api at {self.date_service.parse('now')}",
            )

            return self.get_details_by_contract(
                contract_address,
                network,
            )

        cache.set(
            f'{self.coin_gecko_cache_key}_{network}_{contract_address}',
            coin_gecko_response,
            settings.DISCORD_BOT_FETCH_INTERVAL,
        )

        return coin_gecko_response

    def get_ticker(
        self,
        contract_address: str,
        network: str,
        target_market: str
    ) -> Dict[str, Any]:
        coin_gecko_response = self.get_details_by_contract(
            contract_address,
            network,
        )
        if not coin_gecko_response:
            return None

        data = [
            ticker
            for ticker in coin_gecko_response.get('tickers')
            if ticker.get('market', {}).get('identifier') == target_market
        ]

        if not data:
            return None

        return data[0]
