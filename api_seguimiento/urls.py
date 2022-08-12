from django.contrib import admin
from django.urls import path,include
from .views import consulta

urlpatterns = [
    path('ninio/<agnio>/<mes>/<ipress>',consulta.as_view(),name='consulta'),
]
