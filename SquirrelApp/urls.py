from django.urls import path

from . import views

app_name = 'SquirrelApp'

urlpatterns = [
        path('sightings', views.index, name='index'),
        path('sightings/<str:squirrel_id>', views.sighting_details, name='detail'),
        path('sightings/add', views.add_request, name='add'),

        ]
