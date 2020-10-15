from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'SquirrelApp/index.html', context)

def squirrel_details(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=UniqueSquirrelID)

    context = {
        'squirrel': squirrel,
    }
    return render(request, 'SquirrelApp/detail.html', context)


# Create your views here.
