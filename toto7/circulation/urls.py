from django.urls import path, include
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'circulation'

urlpatterns = [
    path('', index, name='index'),
    path('sign_up/', sign_up, name='sign_up'),
    path('about/', about, name='about'),
    path('rules/', rules, name='rules'),
    path('privacy/', privacy, name='privacy'),
    path('sign_out/', sign_out, name='sign_out'),
    path('sign_in/', sign_in, name='sign_in'),
    path('userinfo/', userinfo, name='userinfo'),
    path('adminpanel/', adminpanel, name='adminpanel'),
    path('match_edit/<str:pk>', match_edit, name='match_edit'),
    path('finish_match_edit/<str:pk>', finish_match_edit, name='finish_match_edit'),
    path('match_delete/<str:pk>', match_delete, name='match_delete'),
    path('сirculation_edit/<str:pk>', сirculation_edit, name='сirculation_edit'),
    path('circulation_archive/', circulation_archive, name='circulation_archive'),
    path('сirculation_delete/<str:pk>', сirculation_delete, name='сirculation_delete'),
    path('ticket_edit/<str:pk>', ticket_edit, name='ticket_edit'),
    path('ticket_delete/<str:pk>', ticket_delete, name='ticket_delete'),
    path('commands/', commands, name='commands'),
    path('commands_edit/<str:pk>', commands_edit, name='commands_edit'),
    path('commands_delete/<str:pk>', commands_delete, name='commands_delete'),
    path('betinfo/', betinfo, name='betinfo'),
    path('betinfo_edit/<str:pk>', betinfo_edit, name='betinfo_edit'),
    path('betinfo_delete/<str:pk>', betinfo_delete, name='betinfo_delete'),

    path("password_reset/", auth_views.PasswordResetView.as_view(template_name='password_reset.html'),
         name="password_reset"),
    path("accounts/password_reset/done/",
         auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
         name="password_reset_done"),
    path("password_change/", auth_views.PasswordChangeView.as_view(template_name='password_change.html'),
         name="password_change"),
    path("accounts/password_change/done/", auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'),
         name="password_change_done"),
    path("reset/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(), name="password_reset_confirm"),
    path("reset/done/", auth_views.PasswordResetCompleteView.as_view(), name="password_reset_complete"),
]
