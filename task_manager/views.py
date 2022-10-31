from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView,
                                  DeleteView, TemplateView)

from task_manager.forms import UserCreationFormCustom
from task_manager.models import TaskStatus
from task_manager.permissions import (UserPermissionsMixin,
                                      StatusLoginRequiredMixin)


class IndexView(TemplateView):
    template_name = "index.html"
    extra_context = {'title': _('Task manager'),
                     'description': _('A simple and functional task manager.'),
                     }


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


class CreateUser(CreateView):
    form_class = UserCreationFormCustom
    template_name = "users/create.html"
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
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "users/update.html"
    login_url = "login"
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('User successfully updated'))
        return reverse_lazy('login')


class DeleteUser(UserPermissionsMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    extra_context = {'title': _('Delete user'),
                     'btn_name': _('Yes, delete'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('User successfully deleted'))
        return reverse_lazy('users')


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "users/login.html"
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


class StatusesList(StatusLoginRequiredMixin, ListView):
    model = TaskStatus
    template_name = "task_statuses/statuses.html"
    context_object_name = "statuses"
    login_url = "login"
    extra_context = {'title': _('Statuses'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateStatus(StatusLoginRequiredMixin, CreateView):
    model = TaskStatus
    fields = ['name']
    template_name = "users/create.html"
    login_url = "login"
    extra_context = {'title': _('Create status'),
                     'btn_name': _('Create')
                     }

    def get_success_url(self):
        messages.info(self.request, _('Status successfully created'))
        return reverse_lazy('statuses')


class UpdateStatus(StatusLoginRequiredMixin, UpdateView):
    model = TaskStatus
    fields = ['name']
    template_name = "users/update.html"
    login_url = "login"
    extra_context = {'title': _('Update status'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Status successfully updated'))
        return reverse_lazy('statuses')


class DeleteStatus(StatusLoginRequiredMixin, DeleteView):
    model = TaskStatus
    template_name = "users/delete.html"
    login_url = "login"
    extra_context = {'title': _('Delete status'),
                     'btn_name': _('Yes, delete'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Status successfully deleted'))
        return reverse_lazy('statuses')
