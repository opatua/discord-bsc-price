from decimal import Decimal
from typing import Any, Dict, Optional, Tuple
from discord.ext import commands

from src.services.coin_gecko_service import CoinGeckoService


class Command(commands.Bot):
    coin_gecko_service = CoinGeckoService()

    def __init__(self):
        super().__init__(command_prefix="!")

        @self.command(name='price', help='please provide BSC token address')
        async def get_price(ctx, network: str, contract_address: str, target_currency: str = 'usd', from_market: str = None):
            contract_details = self.coin_gecko_service.get_details_by_contract(
                contract_address,
                network,
            )
            price, price_from = self.get_price_details(
                contract_details,
                target_currency,
                from_market,
            )
            if not price:
                await ctx.send(
                    f"```Unable to get price from {from_market}.```",
                )

                return None

            await ctx.send(
                f"```Price {contract_details.get('symbol')} {round(Decimal(price), 12):12f} in {target_currency.upper()} from {price_from}```",
            )

        @self.command(name='mcap', help='please provide BSC token address')
        async def get_market_cap(ctx, network: str, contract_address: str, target_currency: str = 'usd', from_market: str = None):
            contract_details = self.coin_gecko_service.get_details_by_contract(
                contract_address,
                network,
            )

            total_supply = contract_details.get(
                'market_data',
                {},
            ).get('total_supply')
            if not total_supply:
                await ctx.send(
                    f"```Unable to calculate market cap.```",
                )

                return None

            price, price_from = self.get_price_details(
                contract_details,
                target_currency,
                from_market
            )

            if not price:
                await ctx.send(
                    f"```Unable to calculate market cap from {from_market}.```",
                )

                return None

            await ctx.send(
                f"```Market cap {contract_details.get('symbol')} {round(Decimal(price) * Decimal(total_supply), 2):,} in {target_currency.upper()} from {price_from}```",
            )

    def get_price_details(
        self,
        contract_details: Dict[str, Any],
        target_currency: str,
        from_market: Optional[str],
    ) -> Tuple[Optional[Decimal], Optional[str]]:
        tickers = contract_details.get('tickers')
        if not tickers:
            return None, None

        ticker = tickers[0]
        if from_market:
            data = [
                datum
                for datum in tickers
                if from_market.lower() in datum.get('market', {}).get('identifier')
            ]
            if not data:
                return None, None

            ticker = data[0]

        price = ticker.get('converted_last', {}).get(target_currency)
        if not price:

            return None, None

        return price, ticker.get('market').get('name')
