import asyncio
import discord

from django.conf import settings

from src.services.coin_gecko_service import CoinGeckoService


class SimplePrice(discord.Client):
    coin_gecko_service = CoinGeckoService()
    channel_id = None
    bot_id = None
    price_id = ''
    vs_currency = ''

    async def status_update(self):
        price_bot = self.get_guild(
            self.channel_id,
        ).get_member(self.bot_id)
        if not price_bot:
            print('Bot not found!')

            return None

        await price_bot.edit(nick=f"Price {self.price_id.title().replace('-',' ')}"[:32])

        while True:
            price = self.coin_gecko_service.get_simple_price(
                self.price_id,
                self.vs_currency,
            )

            if not price:
                print('price not found')

                break

            await self.change_presence(
                activity=discord.Activity(
                    type=discord.ActivityType.watching,
                    name=f'{self.vs_currency.upper()} {price}',
                ),
            )

            await asyncio.sleep(settings.DISCORD_BOT_FETCH_INTERVAL)

    async def on_ready(self):
        self.loop.create_task(self.status_update())
