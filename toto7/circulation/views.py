from django.shortcuts import render


def index(request):
    context = {
        'title': ' '
    }
    return render(request, 'index.html')
