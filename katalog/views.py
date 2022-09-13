from django.shortcuts import render
from katalog.models import CatalogItem

# TODO: Create your views here.


def show_catalog(request):
    data_barang_katalog = CatalogItem.objects.all()
    context = {
        'list_barang': data_barang_katalog,
        'nama': 'Fitria Dwi Cahya',
    }
    return render(request, "katalog.html", context)
