from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import SightingForm
from .models import Sighting

def index(request):
    return render(request, 'SquirrelApp/index.html')

def sightings(request):
    sightings = Sighting.objects.all()
    context = {
            'sightings': sightings,
    }
    return render(request, 'SquirrelApp/sighting.html', context)


def sighting_details(request, sighting_id):
    sighting = get_object_or_404(Sighting, pk=sighting_id)
    return render(request, 'SquirrelApp/detail.html', {'sighting':sighting})


def update_page(request, sighting_id):
    sighting = get_object_or_404(Sighting, pk=sighting_id)
    context = {
            'sighting':sighting,
            }
    return render(request, 'SquirrelApp/update.html', context)


def update_request(request):
    if request.method == 'POST':
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'SquirrelApp/submitted.html')
        else:
            return render(request, 'SquirrelApp/submitfail.html')
    else:
        return {}

def add_page(request):
    return render(request, 'SquirrelApp/add.html')

def map(request):
    return render(request, 'SquirrelApp/map.html')

