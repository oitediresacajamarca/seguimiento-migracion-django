from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cmi/migracion/', include('migracion.urls')),
    path('cmi/api/', include('api_seguimiento.urls')),
]
