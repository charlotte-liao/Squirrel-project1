from django.shortcuts import render

from django.http import HttpResponse

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }


    return render(request, 'SquirrelApp/index.html', context)


# Create your views here.
