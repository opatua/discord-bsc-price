import asyncio
import discord

from django.conf import settings

from src.services.coin_gecko_service import CoinGeckoService


class Price(discord.Client):
    coin_gecko_service = CoinGeckoService()
    channel_id = None
    bot_id = None
    contract_address = None
    network = None
    target_market = None
    target_currency = ''

    async def status_update(self):
        while True:
            price, price_from = self.coin_gecko_service.get_price_details(
                self.coin_gecko_service.get_details_by_contract(
                    self.contract_address,
                    self.network,
                ),
                self.target_currency,
                self.target_market,
            )

            if not price:
                print('price not found')

                break

            await self.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name=f'{price_from} {self.target_currency.upper()} {price}',
                ),
            )

            await asyncio.sleep(settings.DISCORD_BOT_FETCH_INTERVAL)

    async def on_ready(self):
        self.loop.create_task(self.status_update())
