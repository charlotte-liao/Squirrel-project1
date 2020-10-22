from django.urls import path

from . import views

app_name = 'SquirrelApp'

urlpatterns = [
        path('index', views.index, name='index'),
        path('sightings', views.sightings, name='sightings'),
        path('sightings/details/<str:sighting_id>', views.sighting_details, name='detail'),
        path('sightings/add', views.add_page, name='add_page'),
        path('sightings/stats', views.stats, name='stats'),
        path('sightings/<str:squirrel_id>', views.update_page, name='update_page'),
        path('add', views.update_request, name="add"),
        path('update', views.update_request, name="update"),
        path('map',views.map,name='map'),

        ]
       
