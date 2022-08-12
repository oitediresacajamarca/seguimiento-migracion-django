from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('migracion/', include('migracion.urls')),
    path('api/', include('api_seguimiento.urls')),
]
