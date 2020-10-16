from django.forms import ModelForm

from .models import Squirrel

class UpdateRequestForm(ModelForm):
    
    class Meta:
        model = Squirrel
        fields = [
                'Latitude',
                'Longitude',
                'Shift',
                'Date', 
                'Age',
        ]
    
        def save(self, squirrel=None):
            update_request = super(UpdateRequestForm, self).save(commit=False)
            if squirrel:
                update_request.squirrel = squirrel
            update_request.save()
            return update_request
