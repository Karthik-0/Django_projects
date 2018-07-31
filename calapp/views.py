from django.shortcuts import render, get_object_or_404, redirect
from .models import Entry
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import UserCreationForm
from django.views import generic
from .forms import EventForm


def index(request):
    entries = Entry.objects.all()
    return render(request, 'myapp/index.html', {'entries': entries})


@login_required
def details(request, pk):
    entry = Entry.objects.get(id=pk)
    return render(request, 'myapp/details.html', {'entry': entry})


@method_decorator(login_required, name='dispatch')
class AddView(generic.CreateView):
    template_name = 'myapp/form.html'
    model = Entry
    success_url = '/events/dashboard'
    form_class = EventForm


@login_required
def add(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            Entry.objects.create(
                name=name,
                date=date,
                author=request.user,
                description=description
            ).save()
            return HttpResponseRedirect('events/dashboard')
    else:
        form = EventForm()
    return render(request, 'myapp/form.html', {'form': form})


@login_required
def delete(request, pk):
    if request.method == 'DELETE':
        entry = get_object_or_404(Entry, pk=pk)
        print(entry)
        entry.delete()
    return HttpResponseRedirect('events/dashboard')


@login_required
def dashboard(request):
    entries = Entry.objects.filter(user=request.user)
    return render(request, 'myapp/dashboard.html', {'entries': entries})


def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('events/dashboard')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})
