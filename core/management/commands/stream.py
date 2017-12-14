from django.core.management import BaseCommand
from channels import Group
from time import sleep
import os



class Command(BaseCommand):

    help = "Stream all the numbers."

    def handle(self, *args, **options):

        path = '/home/nate/homesite/bin/streams'

        while True:
            for stream in os.listdir(path):
                with open(os.path.join(path,stream)) as file:
                    for ch in file.read():
                        self.transmit(hex(ord(ch))[2:])

    def transmit(self,text,pause=1.25):
        Group('system').send({'text': text})
        sleep(pause)
