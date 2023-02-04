from django.shortcuts import render
from .models import *
from datetime import datetime


def index(request):
    matchs = Match.objects.filter(circulation__end_date__gte=datetime.now())
    return render(request, 'index.html', {'matchs': matchs})


def users(request):
    future = Match.objects.filter(circulation__end_date__gte=datetime.now())
    current = Match.objects.filter(circulation__end_date_current__gte=datetime.now())
    finish = Match.objects.filter(circulation__end_date_current__lte=datetime.now())
    circulation = Circulation.objects.filter(end_date__gte=datetime.now())
    return render(request, 'users.html',
                  {'futures': future,
                   'circulations': circulation,
                   'currents': current,
                   'finishes': finish}, )
