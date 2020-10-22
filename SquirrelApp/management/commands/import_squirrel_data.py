
from django.core.management.base import BaseCommand
import csv
from SquirrelApp.models import Sighting
from datetime import date,datetime

class Command(BaseCommand):
    help="Getting information about squirrels"

    def add_arguments(self,parser):
        parser.add_argument('squirrel_file', help = 'file containing squirrel details')
    


    def handle(self,*args,**options):
        file_=options['squirrel_file']
        def convert_bool(str_):
            if str(str_) in ['TRUE', 'true', 'True']:
                str_ = True
            elif str(str_) in ['FALSE', 'false', 'False']:
                str_ = False
            else:
                str_ = None
            return str_
        with open(file_) as fp:
            reader=csv.DictReader(fp)
            
            for item in reader:

                obj=Sighting()
                obj.Latitude=float(item['X'])
                obj.Longitude = float(item['Y'])
                obj.Shift = item['Shift']
                obj.Date = datetime(int(item['Date'][-4:]),int(item['Date'][:2]), int(item['Date'][2:4]))
                obj.Age = item['Age']
                obj.UniqueSquirrelID = item['Unique Squirrel ID']
                obj.PrimaryFurColor=item['Primary Fur Color']
                obj.Location=item['Location']
                obj.SpecificLocation=item['Specific Location']
                obj.Running=convert_bool(item['Running'])
                obj.Chasing=convert_bool(item['Chasing'])
                obj.Climbing=convert_bool(item['Climbing'])
                obj.Eating=convert_bool(item['Eating'])
                obj.Foraging=convert_bool(item['Foraging'])
                obj.OtherActivities=item['Other Activities']
                obj.Kuks=convert_bool(item['Kuks'])
                obj.Quaas=convert_bool(item['Quaas'])
                obj.Moans=convert_bool(item['Moans'])
                obj.TailFlags=convert_bool(item['Tail flags'])
                obj.TailTwitches=convert_bool(item['Tail twitches'])
                obj.Approaches=convert_bool(item['Approaches'])
                obj.Indifferent=convert_bool(item['Indifferent'])
                obj.RunsFrom=convert_bool(item['Runs from'])
                obj.save()


        msg=f'You are importing from {file_}'
        self.stdout.write(self.style.SUCCESS(msg))


#def receice_data(request):
   # if request_method='POST':
       # form= SquirrelSightingForm(request.POST)
       # if form is valid():
           # form.save()
   # else:
       # retun http200(form.errors)




