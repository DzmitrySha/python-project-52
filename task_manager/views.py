from django.contrib.auth import logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.forms import UserCreationFormCustom
from task_manager.permissions import UserPermissionsMixin


class UsersList(ListView):
    model = User
    template_name = "users.html"
    context_object_name = "users"
    extra_context = {'title': _('Users'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }
    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context.update({'title': _('Users'),
    #                     'btn_update': _('Update'),
    #                     'btn_delete': _('Delete'),
    #                     })
    #     return context


class CreateUser(CreateView):
    form_class = UserCreationFormCustom
    template_name = "create.html"
    success_url = reverse_lazy("login")
    extra_context = {'title': _('Registration user'),
                     'btn_name': _('Register')
                     }
    # автоматический вход пользователя после регистрации:
    # def form_valid(self, form):
    #     user = form.save()
    #     login(self.request, user)
    #     return redirect("home")


class UpdateUser(UserPermissionsMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "update.html"
    login_url = "login"
    success_url = reverse_lazy("login")
    extra_context = {'title': _('Update user'),
                     'btn_name': _('Update'),
                     }
    # permission_required = ('task_manager.view_user',
    #                        'task_manager.change_user'
    #                        )


class DeleteUser(UserPermissionsMixin, DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users")
    extra_context = {'title': _('Delete user'),
                     'btn_name': _('Yes, delete'),
                     }
    # permission_required = ('task_manager.view_user',
    #                        'task_manager.delete_user'
    #                        )


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"
    extra_context = {'title': _('Enter'),
                     'btn_name': _('Enter'),
                     }

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
