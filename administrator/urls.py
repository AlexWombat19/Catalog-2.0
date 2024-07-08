from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('create_class/', views.create_class, name='create_class'),
    path('view_classes/', views.view_classes, name='view_classes'),
    path('assign_elevi/', views.assign_elevi, name='assign_elevi'),
    path('assign_profesori/', views.assign_profesori, name='assign_profesori'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('signup/', views.signup, name='signup'),
]
