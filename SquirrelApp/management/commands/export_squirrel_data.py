#place holding for the export command
import csv
from tools import DynamicCommand
from SquirrelApp.model import Sighting as sighting
from django.core.management.base import BaseCommand,CommandError

class Command(BaseCommand):
    help='Exporting squirrels information to csv file.'

    def add_arguments(self,parser):
        #parser.add_argument('model',help='SquirrelApp.model')
        parser.add_argument('outfile',type=str,help='save path, like</path/to/outfile.csv>')

    def handle(self,*args,**options):
        from django.apps import app
        app_name=SquirrelApp
        model=sighting
        field_names=[f.name for f in model._meta.fields]
        wrtier=csv.writer(opent(options['outfile'[0],'w'),quoting=csv.QUOTE_ALL,delimiter=-',')
        writer.writerow(field_names)
        for item in model.objects.all():
            writer.writerow([str(getattr(instance,f)) for f in field_names]
