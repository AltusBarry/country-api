from django.core.management.base import BaseCommand, CommandError

from countries import utils


class Command(BaseCommand):
    help = "Bootstrap some db data."

    def handle(self, *args, **options):
        utils.bootstrap_data()
