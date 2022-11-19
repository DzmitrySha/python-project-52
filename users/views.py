from django.contrib import messages
from django.contrib.auth.models import User
from django.db.models import ProtectedError
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


class UpdateUser(UserPermissionsMixin, UpdateView):
    model = User
    form_class = UserCreationFormCustom
    template_name = "users/form.html"
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('User successfully updated'))
        return reverse_lazy('users')


class DeleteUser(UserPermissionsMixin, DeleteView):
    model = User
    template_name = "users/delete.html"
    success_url = reverse_lazy('users')
    context_object_name = "user"
    extra_context = {'title': _('Delete user'),
                     'btn_name': _('Yes, delete'),
                     }

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.info(self.request, _('User successfully deleted'))
        except ProtectedError:
            messages.error(
                self.request,
                _('It`s not possible to delete a User that is being used')
            )
        return redirect(success_url)
