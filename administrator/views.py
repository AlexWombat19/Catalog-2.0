from django.shortcuts import render, redirect
from .models import Class
from .forms import ClassForm
from Elevi.models import Elevi
from Elevi.forms import EleviForm
from Profesor.models import Profesor
from Profesor.forms import ProfesorForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate


def create_class(request):
    if request.method == 'POST':
        form = ClassForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_classes')
    else:
        form = ClassForm()
    return render(request, 'administrator/create_class.html', {'form': form})

def view_classes(request):
    classes = Class.objects.all()
    return render(request, 'administrator/view_classes.html', {'classes': classes})


def assign_elevi(request):
    if request.method == 'POST':
        form = EleviForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_students')
    else:
        form = EleviForm()
    return render(request, 'administrator/assign_elevi.html', {'form': form})


def assign_profesori(request):
    if request.method == 'POST':
        form = ProfesorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('view_professors')
    else:
        form = ProfesorForm()
    return render(request, 'administrator/assign_profesori.html', {'form': form})

def profile(request):
    pass

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})