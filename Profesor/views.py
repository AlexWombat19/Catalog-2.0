from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.views.generic import CreateView

from administrator.models import Class
from .forms import GradeForm, AttendanceForm, Profesor
from .models import Grade, Attendance

class ProfesorCreateView(CreateView):
    template_name = 'profesor/profesor_create.html'
    model = Profesor
    fields = '__all__'
    success_url = reverse_lazy('home_page')

@login_required
def add_grade(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            grade = form.save(commit=False)
            grade.teacher = request.user.profesor
            grade.save()
            return redirect('view_teacher_classes')
    else:
        form = GradeForm()
    return render(request, 'teachers/add_grade.html', {'form': form})

@login_required
def mark_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            attendance = form.save(commit=False)
            attendance.teacher = request.user.profesor
            attendance.save()
            return redirect('view_teacher_classes')
    else:
        form = AttendanceForm()
    return render(request, 'teachers/mark_attendance.html', {'form': form})

@login_required
def view_teacher_classes(request):
    classes = Class.objects.all()
    return render(request, 'profesor/view_classes.html', {'classes': classes})