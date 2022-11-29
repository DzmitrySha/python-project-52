from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.messages.views import SuccessMessageMixin
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
    model = get_user_model()
    template_name = "users/users.html"
    context_object_name = "users"
    extra_context = {'title': _('Users'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class UserDetailView(DetailView):
    model = get_user_model()
    template_name = "users/user.html"
    context_object_name = "user"
    extra_context = {'title': _('User'),
                     'tasks': Tasks.objects.all,
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateUser(SuccessMessageMixin, CreateView):
    form_class = UserCreationFormCustom
    template_name = "users/form.html"
    success_message = _('User successfully registered')
    success_url = reverse_lazy('login')
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }


class UpdateUser(SuccessMessageMixin, UserPermissionsMixin, UpdateView):
    model = get_user_model()
    form_class = UserCreationFormCustom
    success_message = _('User successfully updated')
    success_url = reverse_lazy('users')
    template_name = "users/form.html"
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }


class DeleteUser(UserPermissionsMixin, DeleteView):
    model = get_user_model()
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
