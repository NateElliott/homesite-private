from django.core.management import BaseCommand
from channels import Group
from random import randrange
from time import sleep


# The class must be named Command, and subclass BaseCommand
class Command(BaseCommand):

    help = "Stream all the numbers."


    # A command must define handle()
    def handle(self, *args, **options):
        while True:
            params = {
                'text': str(randrange(999, 10000))
            }

            Group('system').send(params)
            sleep(1.5)
