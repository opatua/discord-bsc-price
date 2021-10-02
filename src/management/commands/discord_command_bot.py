from django.conf import settings
from django.core.management.base import BaseCommand

from src.services.discord.command import Command as DiscordCommand


class Command(BaseCommand):
    discord_command = DiscordCommand()

    def add_arguments(self, parser):
        parser.add_argument(
            '--discord_bot_token',
            help='Your discord bot token',
        )

    def handle(self, *args, **options):
        self.discord_command.run(options.get('discord_bot_token'))
