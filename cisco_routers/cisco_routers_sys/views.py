from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from .models import *
from django.views.generic import ListView

# Create your views here.

def Display_Router(request):
    items = Routers.objects.all()
    context = {
        'items': items,
        'header': "Router"
    }
    return render(request, 'index.html', context)


def index(request):
    return render(request, 'index.html')


def Create_router(request):
    if request.method == "POST":
        form = RouterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = RouterForm(request.GET)
        return render(request, "add_new.html", {'form': form})

#Updating routers
def Update_Router(request, pk):
    item = get_object_or_404(Routers, pk=pk)
    if request.method == 'POST':
        form = RouterForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
        return render(request, 'index.html', {'form': form})
    else:
        form = RouterForm(instance=item)
        return render(request, 'edit_item.html', {'form': form})

# Deleting items

def Delete_Router(request, pk):
    Routers.objects.filter(id=pk).delete()
    items = Routers.objects.all()
    context = {
        'items': items,
    }
    return render(request, 'index.html', context)

