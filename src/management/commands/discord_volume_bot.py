from django.core.management.base import BaseCommand

from src.services.discord.volume import Volume


class Command(BaseCommand):
    discord_volume = Volume()

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
            'target_market',
            nargs='?',
            help='Get price from market',
        )
        parser.add_argument(
            'target_currency',
            nargs='?',
            default='usd',
            help='Currency you want to watch lower case example: usd, btc, eth',
        )

    def handle(self, *args, **options):
        channel_id = options.get('channel_id')
        discord_bot_id = options.get('discord_bot_id')
        try:
            self.discord_volume.channel_id = int(
                channel_id,
            )
            self.discord_volume.bot_id = int(
                discord_bot_id,
            )
        except Exception:
            print(
                f'Your channel_id={channel_id} and discord_bot_id={discord_bot_id} must be able convert to integer. Please try again.',
            )

            return None

        self.discord_volume.network = options.get('network')
        self.discord_volume.target_market = options.get(
            'target_market')
        self.discord_volume.target_currency = options.get(
            'target_currency',
        )
        self.discord_volume.contract_address = options.get(
            'contract_address',
        )

        self.discord_volume.run(options.get('discord_bot_token'))
