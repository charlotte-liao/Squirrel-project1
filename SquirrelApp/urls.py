from django.urls import path

from . import views

app_name = 'SquirrelApp'

urlpatterns = [
        path('sightings', views.index, name='index'),
        path('sightings/details/<str:sighting_id>', views.sighting_details, name='detail'),
        path('sightings/add', views.add_page, name='add'),
        path('sightings/str:squirrel_id/<str:sighting_id>', views.update_page, name='update_page'),

        path('update', views.update_request, name="update"),
        path('map',views.map,name='map'),
        ]
