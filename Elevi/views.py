
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Elevi, Class
from Profesor.models import Profesor
from django.conf.global_settings import EMAIL_HOST_USER
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.mail import EmailMessage
from django.template.loader import get_template
from django.urls import reverse_lazy
from django.views.generic import CreateView
from .forms import EleviForm

@login_required
def my_class_view(request):
    elev = Elevi.objects.get(user=request.user)
    class_number = elev.class_number
    professors = Profesor.objects.filter(classes=class_number)
    return render(request, 'elev/my_class.html', {
        'class_number': class_number,
        'professors': professors,
    })

class ElevCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    template_name = 'elev/create_elev.html'
    model = Elevi
    form_class = EleviForm
    success_url = reverse_lazy('home_page')
    permission_required = 'students.add_student'

    def form_valid(self, form):
        if form.is_valid():
            new_student = form.save()
            details_student = {
                'full_name': f'{new_student.first_name} {new_student.last_name}',
            }
            subject = 'Confirmare cont nou!'
            message = get_template('elev/email_confirmation.html').render(details_student)
            mail = EmailMessage(subject, message, EMAIL_HOST_USER, [new_student.email])
            mail.content_subtype = 'html'
            # mail.send()
        return super().form_valid(form)
