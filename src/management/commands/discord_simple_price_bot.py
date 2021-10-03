from django.core.management.base import BaseCommand

from src.services.discord.simple_price import SimplePrice


class Command(BaseCommand):
    discord_simple_price = SimplePrice()

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
            '--price_id',
            help='Your coin to watch',
        )
        parser.add_argument(
            'vs_currency',
            nargs='?',
            default='usd',
            help='Currency you want to watch lower case example: usd, btc, eth',
        )

    def handle(self, *args, **options):
        channel_id = options.get('channel_id')
        discord_bot_id = options.get('discord_bot_id')
        try:
            self.discord_simple_price.channel_id = int(
                channel_id,
            )
            self.discord_simple_price.bot_id = int(
                discord_bot_id,
            )
        except Exception:
            print(
                f'Your channel_id={channel_id} and discord_bot_id={discord_bot_id} must be able convert to integer. Please try again.',
            )

            return None

        self.discord_simple_price.price_id = options.get('price_id')
        self.discord_simple_price.vs_currency = options.get('vs_currency')

        self.discord_simple_price.run(options.get('discord_bot_token'))
