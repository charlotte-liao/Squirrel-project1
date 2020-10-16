from django.forms import ModelForm

from .models import Sighting

class UpdateRequestForm(ModelForm):
    class Meta:
        model = Sighting
        fields = [
                'UniqueSquirrelID',
                'Latitude',
                'Longitude',
                'Shift',
                'Date', 
                'Age',
        ]
   
class AddRequestForm(ModelForm):
    class Meta:
        model = Sighting
        fields = [
                'UniqueSquirrelID',
                'Latitude',
                'Longitude',
                'Shift',
                'Date',
                'Age',
                'PrimaryFurColor',
                'Location',
                'SpecificLocation',
                'Running',
                'Chasing',
                'Climbing',
                'Eating',
                'Foraging',
                'OtherActivities',
                'Kuks',
                'Quaas',
                'Moans',
                'TailFlags',
                'TailTwitches',
                'Approaches',
                'Indifferent',
                'RunsFrom',
        ]
