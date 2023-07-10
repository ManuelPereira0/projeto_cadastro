from django.urls import path
from . import views

urlpatterns = [
    # rota, views responsavel, nome de referencia
    path("", views.index, name="index"),
]