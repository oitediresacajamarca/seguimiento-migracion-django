from  django.urls import path
from .views import migracion_con
urlpatterns=[
    path('migra/',migracion_con.as_view(),name='migra')
]