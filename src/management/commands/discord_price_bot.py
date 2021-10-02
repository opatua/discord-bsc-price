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
            help='Contract address',
        )
        parser.add_argument(
            '--network',
            help='Network address',
        )
        parser.add_argument(
            '--target_market',
            help='Get price from market',
        )
        parser.add_argument(
            '--target_currency',
            help='Currency you want to watch lower case example: usd, btc, eth',
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
                f'Your channel_id={channel_id} and discord_bot_id={discord_bot_id} must be able convert to integer. Please try again.',
            )

            return None

        self.discord_price_service.network = options.get('network')
        self.discord_price_service.target_market = options.get('target_market')
        self.discord_price_service.target_currency = options.get(
            'target_currency',
        )
        self.discord_price_service.contract_address = options.get(
            'contract_address',
        )

        self.discord_price_service.run(options.get('discord_bot_token'))
