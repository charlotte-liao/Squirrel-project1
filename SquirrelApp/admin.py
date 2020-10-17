from django.contrib import admin

from .models import Sighting
from .models import Squirrel

admin.site.register(Sighting)
admin.site.register(Squirrel)
# Register your models here.
