from django.db import models

#class Map(models.Model):
  #return "hello"


class Sighting(models.Model):

    UniqueSquirrelID=models.CharField(
            max_length=100,
            help_text='Unique Squirrel ID',
            blank=False,
            null=False,
    )

    Date=models.DateField(
            help_text='Date',
    )

    def __str__(self):
        return f'{self.id}'


    Latitude = models.FloatField(
            max_length=20,
            help_text='Latitude discovered',
            blank=False,
            null=False,
    )

    Longitude = models.FloatField(
            max_length=20,
            blank=False,
            null=False,
            help_text='Longitude discovered',
    )
   
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
            (AM, 'AM'), 
            (PM, 'PM'),
    ]

    Shift = models.CharField(
            max_length=20,
            help_text='shift',
            choices=SHIFT_CHOICES, 
            default=AM,
            null=True,
    )

    Age = models.CharField(
            max_length=20,
            help_text='Age',
            default=0,
            null=True,
    )

    PrimaryFurColor = models.CharField(
            max_length=20,
            blank = True,
            null=True,
    )

    Location = models.TextField(
            blank = True,
            null=True,
    )
    
    SpecificLocation = models.CharField(
            max_length=100,
            blank = True,
            null=True,
    )

    Running = models.BooleanField(
            blank = True,
            null=True,
    )

    Chasing = models.BooleanField(
            blank = True,
            null=True,
    )
    
    Climbing = models.BooleanField(
            blank = True,
            null=True,
    )

    Eating = models.BooleanField(
            blank = True,
            null=True,
    )

    Foraging = models.BooleanField(
            blank = True,
            null=True,
    )

    OtherActivities = models.CharField(
            max_length = 100,
            blank = True,
            null=True,
    )

    Kuks = models.BooleanField(
            blank = True,
            null=True,
    )

    Quaas = models.BooleanField(
            blank = True,
            null=True,
    )

    Moans = models.BooleanField(
            blank = True,
            null=True,
    )

    TailFlags = models.BooleanField(
            blank = True,
            null=True,
    )

    TailTwitches = models.BooleanField(
            blank = True,
            null=True,
    )

    Approaches = models.BooleanField(
            blank = True,
            null=True,
    )

    Indifferent = models.BooleanField(
            blank = True,
            null=True,
    )

    RunsFrom = models.BooleanField(
            blank = True,
            null=True,
    )

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Sighting._meta.fields]
   


class Squirrel(models.Model):
    UniqueSquirrelID=models.CharField(
            max_length=100,
            primary_key=True,
            help_text='Unique Squirrel ID',
    )

    def __str__(self):
        return self.UniqueSquirrelID
