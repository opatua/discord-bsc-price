from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seeding Hello'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.help)
