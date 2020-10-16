
from django.core.management.base import BaseCommand
import csv
from SquirrelApp.models import Squirrel

class Command(BaseCommand):
    help="Getting information about squirrels"

    def add_arguments(self,parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel details')

    def handle(self,*args,**options):
        file_=options['squirrel_file']
        with open(file_) as fp:
            reader=csv.DictReader(fp)
            for item in reader:
                obj=Squirrel()
                obj.Latitude=item['X']
                obj.Longtitude = item['Y']
                obj.Shift = item['Shift']
                obj.Date = item['Date']
                obj.Age = item['Age']
                obj.UniqueSquirrelID = item['Unique Squirrel ID']
                obj.PrimaryFurColor=item['Primary Fur Color']
                obj.Location=item['Location']
                obj.SpecificLocation=item['Specific Location']
                obj.Running=item['Running']
                obj.Chasing=item['Chasing']
                obj.Climbing=item['Climbing']
                obj.Eating=item['Eating']
                obj.Foraging=item['Foraging']
                obj.OtherActivities=item['Other Activites']
                obj.Kuks=item['Kuks']
                obj.Quaas=item['Quaas']
                obj.Moans=item['Moans']
                obj.TailFlags=item['Tail flags']
                obj.TailTwitches=item['Tail twitches']
                obj.Approaches=item['Approaches']
                obj.Indifferent=item['Indifferent']
                obj.RunsFrom=item['Run from']
                obj.save()


        msg=f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))
