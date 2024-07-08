
from django.urls import path
from . import views

urlpatterns = [
    path('my_class/', views.my_class_view, name='my_class'),
    path('create/', views.ElevCreateView.as_view(), name='create-student'),
]
