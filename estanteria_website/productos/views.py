from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render(request,"home.html")



def productos(request):
    return render(request,"productos.html")



def sucursales(request):
    return render(request,"sucursales.html")


def quienes_somos(request):
    return render(request,"quienessomos.html")