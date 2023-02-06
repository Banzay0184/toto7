from django.contrib.auth.forms import AuthenticationForm
from .models import *


class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('login', 'password')
