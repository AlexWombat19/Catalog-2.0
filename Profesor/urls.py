from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_grade/', views.AddGradeView.as_view(), name='add_grade'),
    path('mark_attendance/', views.MarkAttendanceView.as_view(), name='mark_attendance'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
    path('student_classes/', views.ViewStudentClasses.as_view(), name='view_student_classes'),
    path('teacher_classes/', views.ViewTeacherClasses.as_view(), name='view_teacher_classes'),
    # other paths
]