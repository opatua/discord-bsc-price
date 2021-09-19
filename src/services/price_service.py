from decimal import Decimal
from typing import Any, Dict, Optional
from django.conf import settings

from src.services.third_party_service import ThirdPartyService


class PriceService:
    third_party_service = ThirdPartyService()

    def get_price(self, contract_address: str) -> Optional[Dict[str, Any]]:
        pancake_swap_response = self.third_party_service.call(
            'GET',
            f'{settings.PANCAKESWAP_URL}/tokens/{contract_address}',
            None,
        ).json()
        pancake_data = pancake_swap_response.get('data')

        if not pancake_data:
            return None

        return pancake_data

    def get_market_cap(self, contract_address: str) -> Optional[Decimal]:
        total_supply_response = self.third_party_service.call(
            'GET',
            f'https://api.bscscan.com/api?module=stats&action=tokensupply&contractaddress={contract_address}&apikey={settings.BSC_API_KEY}',
            None,
        ).json()
        total_supply = total_supply_response.get('result')
        if not total_supply:
            return None

        return round(Decimal(self.get_price()) * Decimal(total_supply), 2)
