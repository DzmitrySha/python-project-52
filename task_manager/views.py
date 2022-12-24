from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = 'index.html'
    extra_context = {'title': _('Task manager'),
                     'description': _('A simple and functional task manager.'),
                     }


class LoginUser(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'users/form.html'
    success_message = _('You are logged in.')
    extra_context = {'title': _('Login'),
                     'btn_name': _('Enter'),
                     }

    def get_success_url(self):
        return reverse_lazy('home')

# class LogoutUser(SuccessMessageMixin, LogoutView):
#     template_name = 'index.html'
#     success_message = _('You are logged out.')
#     next_page = reverse_lazy('home')


class LogoutUser(LogoutView):
    def get_success_url(self):
        messages.success(self.request, _('You are logged out.'))
        return reverse_lazy('home')
