from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django import forms

from .models import *


class UserForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField()
    username = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()
    birthday = forms.DateField(widget=forms.DateInput(attrs={
        'type': 'date'
    }))
    region = forms.CharField()
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'tel'
    }))

    class Meta:
        model = User
        fields = 'email', 'first_name', 'username', 'last_name', 'password1', 'password2', 'birthday', 'region', 'phone'


class CirculationForm(forms.ModelForm):
    number = forms.IntegerField()
    end_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local'
    }))
    end_date_current = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local'
    }))
    end_date_finish = forms.DateTimeField(required=False, widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local'
    }))

    class Meta:
        model = Circulation
        fields = 'number', 'end_date', 'end_date_current', 'end_date_finish'


class MatchForm(forms.ModelForm):
    start_data = forms.DateTimeField(widget=forms.DateTimeInput(attrs={
        'type': 'datetime-local'
    }))
    command_a = forms.SelectMultiple()
    command_b = forms.SelectMultiple()
    # result_a = models.IntegerField(null=True, blank=True)
    # result_b = models.IntegerField(null=True, blank=True)
    # winner = models.ForeignKey(to=Command, on_delete=models.CASCADE, related_name="winner", null=True, blank=True)
    tour = forms.CharField(widget=forms.TextInput)
    circulation = forms.SelectMultiple()

    class Meta:
        model = Match
        fields = 'start_data', 'command_a', 'command_b', 'tour', 'circulation'


class TicketForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    price = forms.DecimalField(widget=forms.NumberInput)
    win = forms.DecimalField(widget=forms.NumberInput)

    class Meta:
        model = Ticket
        fields = 'name', 'price', 'win',
