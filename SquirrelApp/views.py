from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import UpdateRequestForm
from .forms import AddRequestForm
from .models import Sighting
from .models import Squirrel

def index(request):
    sighting = Sighting.objects.all()
    context = {
            'sighting': sighting,
    }
    return render(request, 'SquirrelApp/index.html', context)


def sighting_details(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)
    return render(request, 'SquirrelApp/detail.html', {'squirrel':squirrel})


def update_request(request, squirrel_id):
    if request.method == 'POST':
        form = UpdateRequestForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

def add_request(request):
    if request.method == 'POST':
        form = AddRequestForm(data=request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)

    return JsonResponse({}, status=405)






# Create your views here.
