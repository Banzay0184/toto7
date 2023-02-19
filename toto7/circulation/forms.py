from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, UserChangeForm
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


class UserEditForm(UserChangeForm):
    email = forms.EmailField(widget=forms.EmailInput)
    first_name = forms.CharField()
    username = forms.CharField()
    last_name = forms.CharField()
    password1 = forms.CharField(widget=forms.PasswordInput, required=False)
    password2 = forms.CharField(widget=forms.PasswordInput, required=False)
    birthday = forms.DateField(required=False, widget=forms.DateInput(format='%d/%m/%Y', attrs={
        'type': 'date', 'placeholder': 'Select Date',
    }))
    region = forms.CharField()
    phone = forms.CharField(widget=forms.TextInput(attrs={
        'type': 'tel'
    }))
    image = forms.ImageField(required=False, )

    class Meta:
        model = User
        fields = 'email', 'first_name', 'username', 'last_name', 'password1', 'password2', 'birthday', 'region', 'phone', 'image'


class CirculationForm(forms.ModelForm):
    number = forms.IntegerField()
    end_date = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M', attrs={
        'type': 'datetime-local',
        'placeholder': 'Select Date',
    }))
    end_date_current = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={
        'type': 'datetime-local'
    }))
    end_date_finish = forms.DateTimeField(required=False, widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={
        'type': 'datetime-local'
    }))

    class Meta:
        model = Circulation
        fields = ('number', 'end_date', 'end_date_current', 'end_date_finish')


class MatchForm(forms.ModelForm):
    start_data = forms.DateTimeField(widget=forms.DateTimeInput(format='%Y-%m-%d %H:%M',attrs={
        'type': 'datetime-local'
    }))
    command_a = forms.SelectMultiple()
    command_b = forms.SelectMultiple()
    result_a = forms.IntegerField(required=False)
    result_b = forms.IntegerField(required=False)
    winner = forms.SelectMultiple()
    tour = forms.CharField(widget=forms.TextInput)
    circulation = forms.SelectMultiple()

    class Meta:
        model = Match
        fields = 'start_data', 'command_a', 'command_b', 'tour', 'circulation', 'result_a', 'result_b', 'winner'


class MatchFormEdit(forms.ModelForm):
    result_a = forms.IntegerField(required=False)
    result_b = forms.IntegerField(required=False)

    class Meta:
        model = Match
        fields = 'result_a', 'result_b',


class TicketForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    price = forms.DecimalField(widget=forms.NumberInput)
    win = forms.DecimalField(widget=forms.NumberInput)

    class Meta:
        model = Ticket
        fields = 'name', 'price', 'win',


class BetInfoForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput)
    lastname = forms.CharField(widget=forms.TextInput)
    imag = forms.FileField(widget=forms.FileInput, required=False, )
    price = forms.DecimalField(widget=forms.NumberInput)

    class Meta:
        model = BetInfo
        fields = 'username', 'lastname', 'imag', 'price'


class CommandsForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput)
    imag = forms.FileField(widget=forms.FileInput, required=False, )

    class Meta:
        model = Command
        fields = 'name', 'imag',
