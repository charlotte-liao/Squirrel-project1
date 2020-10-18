from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import SightingForm
from .forms import UpdateForm
from .models import Sighting
from .models import Squirrel

def index(request):
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
        form = UpdateForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'SquirrelApp/submitted.html')
        else:
            return render(request, 'SquirrelApp/submitfail.html')
    else:
        return {}

"""
def update(request, squirrel_id):
    if request.method == "POST":
        form = SightingForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'SquirrelApp/submitted.html')
        else:
            return render(request, 'SquirrelApp/submitfail.html')
    sighting = get_object_or_404(Sighting, UniqueSquirrelID=squirrel_id)
    return render(request, 'SquirrelApp/update.html', {'sighting':sighting})
"""


def add_page(request):
    return render(request, 'SquirrelApp/add.html')

def add_request(request):
    if request.method == 'POST':
        form = AddRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)

def map(request):
    return render(request, 'SquirrelApp/map.html')





# Create your views here.
