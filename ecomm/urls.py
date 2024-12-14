

from django.contrib import admin
from django.urls import path,include
from .import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.base,name='base'),
    path('',views.home,name='home'),
    
]
