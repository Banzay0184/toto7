from django.contrib import admin
from django.urls import include, path
from circulation.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('users/', users, name='users'),
]
