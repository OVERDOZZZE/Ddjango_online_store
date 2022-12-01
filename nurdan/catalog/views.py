from django.shortcuts import render
from .models import Catalog
# Create your views here.


def catalog(request):
    catalog = Catalog.objects.order_by('title')
    return render(request, 'catalog/catalog.html', {'catalog' : catalog})


def create(request):
    return render(request, 'catalog/create.html')
