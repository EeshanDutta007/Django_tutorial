
from django.contrib import admin
from django.urls import path
from vege.views import *
from home.views import *

urlpatterns = [
    path('', home),
    path('recipes/', recipes),
    path('contact/', contact),
    path('about/', about),
    path('success/', success),
    path('admin/', admin.site.urls),
]
