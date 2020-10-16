from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.http import JsonResponse
from .forms import UpdateRequestForm

from .models import Squirrel

def index(request):
    squirrels = Squirrel.objects.all()
    context = {
            'squirrels': squirrels,
    }
    return render(request, 'SquirrelApp/index.html', context)

def squirrel_details(request, squirrel_id):
    squirrel = get_object_or_404(Squirrel, pk=squirrel_id)

    return render(request, 'SquirrelApp/detail.html', {'squirrel': squirrel})

def update_request(request, squirrel_id):
    if request.method == 'POST':
        form = UpdateRequestForm(request)
        if form.is_valid():
            squirrel = Squirrel.objects.get(pk=squirrel_id)
            form = UpdateRequestForm(request.POST, instance=squirrel)
            form.save()
            return JsonResponse({})
        else:
            return JsonResponse({'errors': form.errors}, status=400)
    return JsonResponse({}, status=405)

# Create your views here.
