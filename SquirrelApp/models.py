from django.db import models

#class Map(models.Model):
  #return "hello"


class Squirrel(models.Model):
    UniqueSquirrelID=models.CharField(
            max_length=100,
            help_text='Unique Squirrel ID',
        )
    Date=models.DateField(
            help_text='Date',
        )
    LinktoUnique=models.URLField(
            max_length=300,
            unique=True,
        )

    #def get_squirrel(self):
        #return self.Squirrel 
