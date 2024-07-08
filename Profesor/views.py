from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic.edit import FormView
from .forms import GradeForm, AttendanceForm
from .models import Grade, Attendance
from .models import Elevi
from administrator.models import Class
from .models import Profesor

@method_decorator(login_required, name='dispatch')
class AddGradeView(FormView):
    template_name = 'profesor/add_grade.html'
    form_class = GradeForm
    success_url = '/teacher_classes/'  # Change this to the correct URL

    def form_valid(self, form):
        grade = form.save(commit=False)
        grade.teacher = self.request.user.profesor
        grade.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class MarkAttendanceView(FormView):
    template_name = 'profesor/mark_attendance.html'
    form_class = AttendanceForm
    success_url = '/teacher_classes/'  # Change this to the correct URL

    def form_valid(self, form):
        attendance = form.save(commit=False)
        attendance.teacher = self.request.user.profesor
        attendance.save()
        return super().form_valid(form)

@method_decorator(login_required, name='dispatch')
class ViewStudentClasses(View):
    template_name = 'students/view_classes.html'

    def get(self, request, *args, **kwargs):
        student = get_object_or_404(Elevi, user=request.user)
        classes = student.class_number.all()
        return render(request, self.template_name, {'classes': classes})

@method_decorator(login_required, name='dispatch')
class ViewTeacherClasses(View):
    template_name = 'teachers/view_classes.html'

    def get(self, request, *args, **kwargs):
        teacher = get_object_or_404(Profesor, user=request.user)
        classes = teacher.class_numbers.all()
        return render(request, self.template_name, {'classes': classes})
