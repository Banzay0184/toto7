from django.urls import path
from .views import *

app_name = 'circulation'

urlpatterns = [
    path('', index, name='index'),
    path('sign_up/', sign_up, name='sign_up'),
    path('sign_out/', sign_out, name='sign_out'),
    path('sign_in/', sign_in, name='sign_in'),
    path('userinfo/', userinfo, name='userinfo'),
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('match_edit/<str:pk>', match_edit, name='match_edit'),
    path('finish_match_edit/<str:pk>', finish_match_edit, name='finish_match_edit'),
    path('match_delete/<str:pk>', match_delete, name='match_delete'),
    path('сirculation_edit/<str:pk>', сirculation_edit, name='сirculation_edit'),
    path('сirculation_delete/<str:pk>', сirculation_delete, name='сirculation_delete'),
    path('ticket_edit/<str:pk>', ticket_edit, name='ticket_edit'),
    path('ticket_delete/<str:pk>', ticket_delete, name='ticket_delete'),
]
