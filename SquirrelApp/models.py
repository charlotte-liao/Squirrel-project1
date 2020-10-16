from django.db import models

#class Map(models.Model):
  #return "hello"


class Squirrel(models.Model):
    UniqueSquirrelID=models.CharField(
            max_length=100,
            help_text='Unique Squirrel ID',
            primary_key = True
    )

    Date=models.DateField(
            help_text='Date',
    )

    def __str__(self):
        return self.UniqueSquirrelID


    Latitude = models.CharField(
            max_length=20,
            blank = True,
            help_text='Latitude discovered',
    )

    Longitude = models.CharField(
            max_length=20,
            blank = True,
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
    )

    Age = models.CharField(
            max_length=20,
            help_text='Age',
            default=0,
    )

    PrimaryFurColor = models.CharField(
            max_length=20,
            blank = True,
    )

    Location = models.TextField(
            blank = True,
    )
    
    SpecificLocation = models.CharField(
            max_length=100,
            blank = True,
    )

    Running = models.BooleanField(
            blank = True,
    )

    Chasing = models.BooleanField(
            blank = True,
    )
    
    Climbing = models.BooleanField(
            blank = True,
    )

    Eating = models.BooleanField(
            blank = True,
    )

    Foraging = models.BooleanField(
            blank = True,
    )

    OtherActivities = models.CharField(
            max_length = 100,
            blank = True,
    )

    Kuks = models.BooleanField(
            blank = True,
    )

    Quaas = models.BooleanField(
            blank = True,
    )

    Moans = models.BooleanField(
            blank = True,
    )

    TailFlags = models.BooleanField(
            blank = True,
    )

    TailTwitches = models.BooleanField(
            blank = True,
    )

    Approaches = models.BooleanField(
            blank = True,
    )

    Indifferent = models.BooleanField(
            blank = True,
    )

    RunsFrom = models.BooleanField(
            blank = True,
    )
    
