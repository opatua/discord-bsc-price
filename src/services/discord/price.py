import asyncio
import discord

from decimal import Decimal
from django.conf import settings

from src.services.price_service import PriceService


class Price(discord.Client):
    price_service = PriceService()
    channel_id = None
    bot_id = None
    contract_address = None

    async def status_update(self):
        currency = self.price_service.get_price(self.contract_address)
        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=currency.get(
                    'symbol',
                ),
            ),
        )
        while True:
            price_bot = self.get_guild(
                self.channel_id,
            ).get_member(self.bot_id)
            if not price_bot:
                print('Bot not found!')

                break

            await price_bot.edit(nick=f"{round(Decimal(self.price_service.get_price(self.contract_address).get('price')), 12):12f}")
            await asyncio.sleep(settings.DISCORD_BOT_FETCH_INTERVAL)

    async def on_ready(self):
        self.loop.create_task(self.status_update())
