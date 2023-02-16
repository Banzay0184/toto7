from pprint import pprint

from django.shortcuts import render, redirect
from datetime import datetime
from .models import *
from django.db.models import Q
from .forms import *
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    match = Match.objects.filter(circulation__end_date_current__gte=datetime.now())
    ticket = Ticket.objects.all()
    betform = MatchForm()
    user_bet = User.objects.all()
    return render(request, 'index.html', {'match': match, 'ticket': ticket, 'betform': betform, 'user_bet': user_bet}, )


def sign_up(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('circulation:index')
    else:
        form = UserForm()
    return render(request, 'sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        print('erro' * 30)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('circulation:index')
    else:
        form = AuthenticationForm()
    return render(request, 'sign_in.html', {'form': form})


def sign_out(request):
    logout(request)
    return redirect('circulation:index')


def about(request):
    return render(request, 'about.html')


def rules(request):
    return render(request, 'rules.html')


def privacy(request):
    return render(request, 'privacy.html')


@login_required(login_url='/login')


def adminpanel(request):
    if request.user.role != 'ADMIN':
        return redirect('circulation:index')
    ticket = Ticket.objects.all()
    future = Match.objects.filter(circulation__end_date__gte=datetime.now())
    current = Match.objects.filter(circulation__end_date_current__gte=datetime.now())
    finish = Match.objects.filter(circulation__end_date_finish__gte=datetime.now())
    circulation = Circulation.objects.filter(end_date_finish__gte=datetime.now())
    users = User.objects.all()
    users_count = User.objects.count()

    # start search
    search = request.GET.get('search')
    users = users.filter(
        Q(username__icontains=search) | Q(first_name__icontains=search) | Q(
            last_name__icontains=search)) if search else users
    # end search

    # start circulation_form
    circulation_form = CirculationForm(request.POST or None)
    if request.method == 'POST' and circulation_form.is_valid():
        circulation_form.save()
        return redirect('circulation:adminpanel')
    circulation_form = CirculationForm()
    # end circulation_form

    # start match_form
    match_form = MatchForm(request.POST or None)
    if request.method == 'POST' and match_form.is_valid():
        match_form.save()
        return redirect('circulation:adminpanel')
    match_form = MatchForm()
    # end match_form

    # start ticket_Form
    ticket_form = TicketForm(request.POST or None)
    if request.method == 'POST' and ticket_form.is_valid():
        ticket_form.save()
        return redirect('circulation:adminpanel')
    ticket_form = TicketForm()
    # end ticket_Form

    return render(request, 'adminpanel.html',
                  {'futures': future,
                   'circulations': circulation,
                   'currents': current,
                   'finishes': finish,
                   'users': users,
                   'users_count': users_count,
                   'circulation_form': circulation_form,
                   'match_form': match_form,
                   'ticket': ticket,
                   'ticket_form': ticket_form,
                   }, )


def userinfo(request):
    # start users_form
    if request.method == 'POST':
        users_form = UserEditForm(request.POST, request.FILES, instance=request.user, )
        if users_form.is_valid():
            users_form.save()
    else:
        users_form = UserEditForm(instance=request.user)
    # end users_form

    return render(request, 'userinfo.html', {'users_form': users_form})


def сirculation_edit(request, pk):
    сirculation = Circulation.objects.get(pk=pk)
    form = CirculationForm(request.POST or None, instance=сirculation)
    if form.is_valid():
        form.save()
        return redirect('circulation:adminpanel')
    return render(request, 'сirculation_edit.html', {'form': form, 'сirculation': сirculation})


def сirculation_delete(request, pk):
    с_delete = Circulation.objects.get(pk=pk)
    с_delete.delete()
    return redirect('circulation:adminpanel')


def circulation_archive(request):
    archive = Match.objects.filter(circulation__end_date_finish__lte=datetime.now())
    circulation = Circulation.objects.filter(end_date_finish__lte=datetime.now())
    return render(request, 'circulation_archive.html', {'archive': archive, 'circulation': circulation})


def match_edit(request, pk):
    match = Match.objects.get(pk=pk)
    form = MatchForm(request.POST or None, instance=match)
    if form.is_valid():
        form.save()
        return redirect('circulation:adminpanel')
    return render(request, 'match_edit.html', {'form': form, 'match': match})


def finish_match_edit(request, pk):
    match = Match.objects.get(pk=pk)
    form = MatchFormEdit(request.POST or None, instance=match)
    if form.is_valid():
        form.save()
        if match.result_a < match.result_b:
            match.winner = match.command_b
            match.draw = False
            match.save()
        if match.result_a > match.result_b:
            match.winner = match.command_a
            match.draw = False
            match.save()
        if match.result_a == match.result_b:
            match.winner = None
            match.draw = True
            match.save()

        return redirect('circulation:adminpanel')
    return render(request, 'finish_match_edit.html', {'form': form, 'match': match})


def match_delete(request, pk):
    m_delete = Match.objects.get(pk=pk)
    m_delete.delete()
    return redirect('circulation:adminpanel')


def ticket_edit(request, pk):
    ticket = Ticket.objects.get(pk=pk)
    form = TicketForm(request.POST or None, instance=ticket)
    if form.is_valid():
        form.save()
        return redirect('circulation:adminpanel')
    return render(request, 'ticket_edit.html', {'form': form, 'ticket': ticket})


def ticket_delete(request, pk):
    t_delete = Ticket.objects.get(pk=pk)
    t_delete.delete()
    return redirect('circulation:adminpanel')


def commands(request):
    commands = Command.objects.all()
    form = CommandsForm(request.POST, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        print('40' * 30)
        form.save()
        return redirect('circulation:commands')
    form = CommandsForm()
    return render(request, 'commands.html', {'commands': commands, 'form': form})


def commands_edit(request, pk):
    commands = Command.objects.get(pk=pk)
    form = CommandsForm(request.POST or None, instance=commands)
    if form.is_valid():
        form.save()
        return redirect('circulation:commands')
    return render(request, 'command_edit.html', {'form': form, 'commands': commands})


def commands_delete(request, pk):
    c_delete = Command.objects.get(pk=pk)
    c_delete.delete()
    return redirect('circulation:commands')
