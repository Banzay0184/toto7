from django.shortcuts import render, redirect
from .models import *
from datetime import datetime
from django.contrib import auth
from .forms import *
from .models import *
from django.contrib.auth import login


def index(request):
    # if request.user.role == 'admin':
    #     return render(request, 'admin.html', {})
    # print('*' * 40)
    # print(request.user)
    matchs = Match.objects.filter(circulation__end_date_current__gte=datetime.now())
    return render(request, 'index.html', {'matchs': matchs })


def superadmin(request):
    future = Match.objects.filter(circulation__end_date__gte=datetime.now())
    current = Match.objects.filter(circulation__end_date_current__gte=datetime.now())
    finish = Match.objects.filter(circulation__end_date_current__lte=datetime.now())
    circulation = Circulation.objects.filter(end_date__gte=datetime.now())
    return render(request, 'users.html',
                  {'futures': future,
                   'circulations': circulation,
                   'currents': current,
                   'finishes': finish}, )


# Create your views here.

def sign_in(request):
    print('signin')
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('circulation:index')
    form = UserLoginForm()
    return render(request, 'sign-in.html', {'form': form})


def registration(request):
    return render(request, 'base.html')
