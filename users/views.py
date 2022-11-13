from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (
    ListView, CreateView, UpdateView, DeleteView, DetailView
)

from tasks.models import Tasks
from users.forms import UserCreationFormCustom
from users.permissions import UserPermissionsMixin


class UsersList(ListView):
    model = User
    template_name = "users/users.html"
    context_object_name = "users"
    extra_context = {'title': _('Users'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }
    # добавление дополнительных данных
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({'title': _('Users'),
    #                     'btn_update': _('Update'),
    #                     'btn_delete': _('Delete'),
    #                     })
    #     return context


class OneUserView(DetailView):
    model = User
    template_name = "users/user.html"
    context_object_name = "user"
    tasks = Tasks.objects.all
    extra_context = {'title': _('User'),
                     'tasks': tasks,
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateUser(CreateView):
    form_class = UserCreationFormCustom
    template_name = "users/form.html"
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }

    def get_success_url(self):
        messages.info(self.request, _('User successfully registered'))
        return reverse_lazy('login')

    # автоматический вход пользователя после регистрации:
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect("home")


class UpdateUser(UserPermissionsMixin, UpdateView):
    model = User
    form_class = UserCreationFormCustom
    template_name = "users/form.html"
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('User successfully updated'))
        return reverse_lazy('login')


class DeleteUser(UserPermissionsMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    context_object_name = "user"
    extra_context = {'title': _('Delete user'),
                     'btn_name': _('Yes, delete'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('User successfully deleted'))
        return reverse_lazy('users')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "users/form.html"
    extra_context = {'title': _('Enter'),
                     'btn_name': _('Enter'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('You are logged in.'))
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    messages.info(request, _('You are logged out.'))
    return redirect('home')
