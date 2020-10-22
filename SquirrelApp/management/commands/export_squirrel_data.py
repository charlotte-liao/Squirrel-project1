import csv

from django.core.management.base import BaseCommand
from SquirrelApp.models import Sighting


class Command(BaseCommand):

    def add_arguments(self,parser):
        parser.add_argument('path')

    def handle(self, *args, **options):
        with open(options['path'][0],'w') as fp:
            export_writer = csv.DictWriter(
                    fp,
                    delimiter=',',
                    fieldnames=[
                        'X',
                        'Y',
                        'Unique Squirrel ID',
                        'Shift',
                        'Date',
                        'Age',
                        'Primary Fur Color',
                        'Location',
                        'Specific Location',
                        'Running',
                        'Chasing',
                        'Climbing',
                        'Eating',
                        'Foraging',
                        'Other Activities',
                        'Kuks',
                        'Quaas',
                        'Moans',
			'Tail flags',
                        'Tail twitches',
                        'Approaches',
                        'Indifferent',
                        'Runs from',
                        ]
                    )
            export_writer.writeheader()

            for row in Sighting.objects.all():
                export_writer.writerow({
                    'X':row.Longitude,
                    'Y':row.Latitude,
                    'Unique Squirrel ID':row.UniqueSquirrelID,
                    'Shift':row.Shift,
                    'Date':row.Date,
                    'Age':row.Age,
                    'Primary Fur Color':row.PrimaryFurColor,
                    'Location':row.Location,
                    'Specific Location':row.SpecificLocation,
                    'Running':row.Running,
                    'Chasing':row.Chasing,
                    'Climbing':row.Climbing,
                    'Eating':row.Eating,
                    'Foraging':row.Foraging,
                    'Other Activities':row.OtherActivities,
                    'Kuks':row.Kuks,
                    'Quaas':row.Quaas,
                    'Moans':row.Moans,
                    'Tail flags':row.TailFlags,
                    'Tail twitches':row.TailTwitches,
                    'Approaches':row.Approaches,
		    'Indifferent':row.Indifferent,
                    'Runs from':row.RunsFrom,
                    })

            msg=f'Export Succeed!'
            self.stdout.write(self.style.SUCCESS(msg))
