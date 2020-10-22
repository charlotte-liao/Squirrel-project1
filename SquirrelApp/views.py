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
    sightings = Sighting.objects.all()[:100]
    context = {
            'sightings':sightings,
    }
    return render(request, 'SquirrelApp/map.html', context)

def stats(request):
    sightings=Sighting.objects.all()
    running_c=0
    chasing_c=0
    eating_c=0
    foraging_c=0
    adult_c=0
    for s in sightings:
        if s.Age == "Adult":
            adult_c+=1
        if s.Running == True:
            running_c+=1
        if s.Chasing == True:
            chasing_c+=1
        if s.Eating == True:
            eating_c+=1
        if s.Foraging == True:
            foraging_c+=1
    context={
            'AdultCounts':adult_c,
            'NumRunning':running_c,
            'NumChasing':chasing_c,
            'NumEating':eating_c,
            'NumForaging':foraging_c,
            }
    return render(request,'SquirrelApp/stats.html',context)
