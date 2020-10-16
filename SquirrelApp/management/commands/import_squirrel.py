
from django.core.management.base import BaseCommand
import csv
from SquirrelApp.models import Squirreldetail

class Command(BaseCommand):
    help="Getting information about squirrels"

    def add_arguments(self,parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel details')

    def handle(self,*args,**options):
        file_=options['squirrel_file']
        with open(file_) as fp:
            reader=csv.DictReader(fp)
            for item in reader:
                obj=Squirreldetail()
                obj.latitude=item['X']
                obj.longtitude = item['Y']
                obj.shift = item['Shift']
                obj.date = item['Date']
                obj.age = item['Age']
                obj.uniqueid = item['Unique Squirrel ID']
                obj.save()

        msg=f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
