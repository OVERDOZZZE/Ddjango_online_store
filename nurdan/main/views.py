from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'main/index.html')


def catalog(request):
    return render(request, 'catalog/catalog.html')


def about(request):
    return render(request, 'main/about.html')



