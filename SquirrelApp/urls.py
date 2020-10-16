from django.urls import path

from . import views

app_name = 'SquirrelApp'

urlpatterns = [
        path('sightings', views.index, name='index'),
        path('sightings/<str:squirrel_id>', views.squirrel_details, name='details'),
        path('update/', views.update_request, name='update_request'),
        ]
