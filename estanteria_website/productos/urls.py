from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name="home"),
    path('productos/',views.productos,name="productos"),
    path('sucursales/',views.sucursales,name="sucursales"),
    path('quienes_somos/',views.quienes_somos,name="quienes"),
]
