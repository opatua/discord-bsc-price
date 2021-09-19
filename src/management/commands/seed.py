from django.core.management import call_command
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeding data'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.help)

        call_command('hello')