from django.shortcuts import render, redirect
from .models import Catalog
from .forms import CatalogForm
from django.views.generic import DetailView, UpdateView
# Create your views here.


class CatalogUpdateView(UpdateView):
    model = Catalog
    template_name = 'catalog/create.html'
    # fields = ['title', 'description', 'price']

    form_class = CatalogForm


class CatalogDetailView(DetailView):
    model = Catalog
    template_name = 'catalog/details_view.html'
    context_object_name = 'article'


def catalog(request):
    catalog = Catalog.objects.order_by('title')
    return render(request, 'catalog/catalog.html', {'catalog' : catalog})


def create(request):
    error = ''
    if request.method == 'POST':
        form = CatalogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Неверная форма'

    form = CatalogForm()

    data = {
        'form': form,
        'error': error
        }

    return render(request, 'catalog/create.html', data)

