from django.core.management.base import BaseCommand

from src.services.discord.price import Price


class Command(BaseCommand):
    discord_price_service = Price()

    def add_arguments(self, parser):
        parser.add_argument(
            '--channel_id',
            help='Your discord channel id',
        )
        parser.add_argument(
            '--discord_bot_token',
            help='Your discord bot token',
        )
        parser.add_argument(
            '--discord_bot_id',
            help='Your discord bot id',
        )
        parser.add_argument(
            '--contract_address',
            help='BSC contract address',
        )

    def handle(self, *args, **options):
        channel_id = options.get('channel_id')
        discord_bot_id = options.get('discord_bot_id')
        try:

            self.discord_price_service.channel_id = int(
                channel_id,
            )
            self.discord_price_service.bot_id = int(
                discord_bot_id,
            )
        except Exception:
            print(
                f'Your channel_id={channel_id} and discord_bot_id={discord_bot_id} must be able convert to integer. Please try again',
            )

            return None

        self.discord_price_service.contract_address = options.get(
            'contract_address',
        )
        self.discord_price_service.run(options.get('discord_bot_token'))
