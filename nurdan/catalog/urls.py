from django.urls import path
from . import views

urlpatterns = [
    path('', views.catalog, name= 'catalog'),
    path('create', views.create, name="create"),
    path('<int:pk>', views.CatalogDetailView.as_view(), name='catalog-detail'),
    # path('<int:pk>/update', views.CatalogUpdateView.as_view(), name='catalog-detail'),
]
