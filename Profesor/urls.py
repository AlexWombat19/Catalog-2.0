from django.urls import path
from . import views
from Elevi.views import Elevi
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('add_grade/', views.add_grade, name='add_grade'),
    path('mark_attendance/', views.mark_attendance, name='mark_attendance'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    # path('signup/', views.signup, name='signup'),
    # path('student_classes/', views.view_student_classes, name='view_student_classes'),
    path('teacher_classes/', views.view_teacher_classes, name='view_teacher_classes'),
]