from discord.ext import commands

from src.services.coin_gecko_service import CoinGeckoService


class Command(commands.Bot):
    coin_gecko_service = CoinGeckoService()

    def __init__(self):
        super().__init__(command_prefix="!")

        @self.command(name='price', help='Please provide contract address, network. To check network with `!networks`')
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
                f"```{contract_details.get('symbol')} price {target_currency.upper()} {price} from {price_from}```",
            )

        @self.command(name='mcap', help='Please provide contract address, network. To check network with `!networks`')
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
                f"```Market cap {contract_details.get('symbol')} {target_currency.upper()} {market_cap} from {price_from}```",
            )

        @self.command(name='volume', help='Please provide contract address, network. To check network with `!networks`')
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
                f"```Volume {contract_details.get('symbol')} {target_currency.upper()} {volume} from {price_from}```",
            )

        @self.command(name='networks', help='Get all available networks')
        async def get_networks(ctx):
            await ctx.send(
                f"Networks:\n```{self.coin_gecko_service.get_networks()}```",
            )

        @self.command(name='commands')
        async def get_commands(ctx):
            helps = [
                'To check price use `!price` with optional value target currency such as `usd, btc, and eth` and target market like `pancakeswap, raydium, etc`, example\n```!price binance-smart-chain 0x4a8a99ac4e7973d20eb9e64db8eb94781dc80ba0```',
                'To check market cap use `!mcap` with optional value target currency such as `usd, btc, and eth` and target market like `pancakeswap, raydium, etc`, example\n```!mcap binance-smart-chain 0x4a8a99ac4e7973d20eb9e64db8eb94781dc80ba0```',
                'To check volume use `!volume` with optional value target currency such as `usd, btc, and eth` and target market like `pancakeswap, raydium, etc`, example\n```!volume binance-smart-chain 0x4a8a99ac4e7973d20eb9e64db8eb94781dc80ba0```',
                'To get all available networks `!networks`',
            ]
            await ctx.send('\n\n'.join(helps))
