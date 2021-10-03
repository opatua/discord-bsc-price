from decimal import Decimal
from typing import Any, Dict, Optional, Tuple
from discord.ext import commands

from src.services.coin_gecko_service import CoinGeckoService


class Command(commands.Bot):
    coin_gecko_service = CoinGeckoService()

    def __init__(self):
        super().__init__(command_prefix="!")

        @self.command(name='price', help='please provide contract address, network')
        async def get_price(ctx, network: str, contract_address: str, target_currency: str = 'usd', target_market: str = None):
            contract_details = self.coin_gecko_service.get_details_by_contract(
                contract_address,
                network,
            )
            price, price_from = self.coin_gecko_service.get_price_details(
                contract_details,
                target_currency,
                target_market,
            )
            if not price:
                await ctx.send(
                    f"```Unable to get price from {target_market}.```",
                )

                return None

            await ctx.send(
                f"```{contract_details.get('symbol')} price {price} in {target_currency.upper()} from {price_from}```",
            )

        @self.command(name='mcap', help='please provide contract address, network')
        async def get_market_cap(ctx, network: str, contract_address: str, target_currency: str = 'usd', target_market: str = None):
            contract_details = self.coin_gecko_service.get_details_by_contract(
                contract_address,
                network,
            )

            market_cap, price_from = self.coin_gecko_service.get_market_cap(
                contract_details,
                target_currency,
                target_market,
            )
            if not market_cap:
                await ctx.send(
                    f"```Unable to calculate market cap.```",
                )

                return None

            await ctx.send(
                f"```Market cap {contract_details.get('symbol')} {market_cap} in {target_currency.upper()} from {price_from}```",
            )

        @self.command(name='volume', help='please provide contract address, network')
        async def get_volume(ctx, network: str, contract_address: str, target_currency: str = 'usd', target_market: str = None):
            contract_details = self.coin_gecko_service.get_details_by_contract(
                contract_address,
                network,
            )

            volume, price_from = self.coin_gecko_service.get_volume(
                contract_details,
                target_currency,
                target_market,
            )
            if not volume:
                await ctx.send(
                    f"```Unable to calculate market cap.```",
                )

                return None

            await ctx.send(
                f"```Volume {contract_details.get('symbol')} {volume} in {target_currency.upper()} from {price_from}```",
            )
