
from django.contrib import admin
from django.urls import path, include
from galeria.views import index
import galeria.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('galeria.urls'), name='index'),
]
