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
        price_bot = self.get_guild(
            self.channel_id,
        ).get_member(self.bot_id)
        if not price_bot:
            print('Bot not found!')

            return None

        contract_details = self.coin_gecko_service.get_details_by_contract(
            self.contract_address,
            self.network,
        )

        ticker = self.coin_gecko_service.get_ticker(
            contract_details,
            self.target_market
        )
        if not ticker:
            return None

        await price_bot.edit(nick=f"Price {contract_details.get('symbol').upper()} {ticker.get('market', {}).get('name')}")

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
                    name=f'{self.target_currency.upper()} {price}',
                ),
            )

            await asyncio.sleep(settings.DISCORD_BOT_FETCH_INTERVAL)

    async def on_ready(self):
        self.loop.create_task(self.status_update())
