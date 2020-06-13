from django.core.management.base import BaseCommand

class Command(BaseCommand):
    def handle(self, *args, **options):
        # TODO: 実装
        print('test command')