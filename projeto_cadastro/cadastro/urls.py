"""
URL configuration for cadastro project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app_cadastro import views

urlpatterns = [
    # rota, views responsavel, nome de referencia
    path("", views.index, name="index"),
    path("usuarios/", views.usuarios, name="cadastro_usuarios"),
    path("lista_usuarios/", views.lista_usuarios, name="lista_usuarios"),
    path("editar/<int:id>", views.editar, name="editar"),
    path("update_usuarios/<int:id>", views.update_usuarios, name="editar_usuarios"),
    path("deletar_usuarios/<int:id>", views.deletar_usuarios, name="deletar_usuarios"),
    path("admin/", admin.site.urls),
]
