from django.urls import path
from . import views
from .views import index, sign_in

app_name = 'circulation'

urlpatterns = [
    path('', index, name='index'),
    path('sign_in/', sign_in, name='sign_in'),
    # path('', sign_in, name='sign_in'),
    path('admin/', views.superadmin, name='index'),
]
