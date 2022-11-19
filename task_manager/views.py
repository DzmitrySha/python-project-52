from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.utils.translation import gettext_lazy as _


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {'title': _('Task manager'),
                     'description': _('A simple and functional task manager.'),
                     }


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "users/form.html"
    extra_context = {'title': _('Login'),
                     'btn_name': _('Enter'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('You are logged in.'))
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out.'))
    return redirect('home')
