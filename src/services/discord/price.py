import asyncio
import discord

from decimal import Decimal
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
        contract_details = self.coin_gecko_service.get_details_by_contract(
            self.contract_address,
            self.network,
        )
        ticker = self.coin_gecko_service.get_ticker(
            self.contract_address,
            self.network,
            self.target_market,
        )
        if not ticker:
            return None

        await self.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, name=f"{contract_details.get('symbol')} in {self.target_currency.upper()}",
            ),
        )
        while True:
            price_bot = self.get_guild(
                self.channel_id,
            ).get_member(self.bot_id)
            if not price_bot:
                print('Bot not found!')

                break

            ticker = self.coin_gecko_service.get_ticker(
                self.contract_address,
                self.network,
                self.target_market,
            )

            price = ticker.get('converted_last', {}).get(self.target_currency)
            if not price:
                print('price not found')

                break

            await price_bot.edit(nick=f"{round(Decimal(price), 12):12f}".rstrip('0'))
            await asyncio.sleep(settings.DISCORD_BOT_FETCH_INTERVAL)

    async def on_ready(self):
        self.loop.create_task(self.status_update())
