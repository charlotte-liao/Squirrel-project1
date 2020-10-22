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
            blank=True,
            null=True,
    )

    def __str__(self):
        return f'{self.id}'


    Latitude = models.FloatField(
            max_length=20,
            help_text='Latitude',
            blank=False,
            null=False,
    )

    Longitude = models.FloatField(
            max_length=20,
            blank=False,
            null=False,
            help_text='Longitude',
    )
   
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
            (AM, 'AM'), 
            (PM, 'PM'),
    ]

    Shift = models.CharField(
            max_length=20,
            help_text='Shift',
            choices=SHIFT_CHOICES, 
            default=AM,
            null=True,
            blank=True, 
    )

    Age = models.CharField(
            max_length=20,
            help_text='Age',
            default=0,
            null=True,
            blank=True,
    )

    PrimaryFurColor = models.CharField(
            max_length=20,
            blank = True,
            null=True,
            help_text="Primary Fur Color",
    )

    Location = models.TextField(
            blank = True,
            null=True,
            help_text="Location",
    )
    
    SpecificLocation = models.CharField(
            max_length=100,
            blank = True,
            null=True,
            help_text="Specific Location",
    )

    Running = models.BooleanField(
            blank=True,
            null=True,
            help_text="Running",
    )

    Chasing = models.BooleanField(
            blank=True,
            null=True,
            help_text="Chasing",
    )
    
    Climbing = models.BooleanField(
            blank=True,
            null=True,
            help_text="Climbing",
    )

    Eating = models.BooleanField(
            blank=True,
            null=True,
            help_text="Eating",
    )

    Foraging = models.BooleanField(
            blank=True,
            null=True,
            help_text="Foraging",
    )

    OtherActivities = models.CharField(
            max_length = 100,
            blank=True,
            null=True,
            help_text="Other Activities",
    )

    Kuks = models.BooleanField(
            blank=True,
            null=True,
            help_text="Kuks",
    )

    Quaas = models.BooleanField(
            blank=True,
            null=True,
            help_text="Quaas",
    )

    Moans = models.BooleanField(
            blank=True,
            null=True,
            help_text="Moans",
    )

    TailFlags = models.BooleanField(
            blank=True,
            null=True,
            help_text="Tail Flags",
    )

    TailTwitches = models.BooleanField(
            blank=True,
            null=True,
            help_text="Tail Twiches",
    )

    Approaches = models.BooleanField(
            blank=True,
            null=True,
            help_text="Approaches",
    )

    Indifferent = models.BooleanField(
            blank=True,
            null=True,
            help_text="Indifferent",
    )

    RunsFrom = models.BooleanField(
            blank=True,
            null=True,
            help_text="Runs From",
    )

    def get_fields(self):
        l = list()
        for field in Sighting._meta.fields:
            if field.name=="id":
                l.append((field.name, field.value_to_string(self)))
            else:
                l.append((field.help_text, field.value_to_string(self)))
        return l   


class Squirrel(models.Model):
    UniqueSquirrelID=models.CharField(
            max_length=100,
            primary_key=True,
            help_text='Unique Squirrel ID',
    )

    def __str__(self):
        return self.UniqueSquirrelID
