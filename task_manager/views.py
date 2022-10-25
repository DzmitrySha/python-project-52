from django.contrib.auth import logout, login
from django.contrib.auth.forms import AuthenticationForm
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.forms import UserCreationFormCustom
from task_manager.permissions import UserPermissionsMixin


class UsersList(ListView):
    model = User
    template_name = "users.html"
    context_object_name = "users"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = _('Users')
        context['title'] = 'Пользователи'
        context['btn_update'] = 'Изменить'
        context['btn_delete'] = 'Удалить'
        return context


class CreateUser(CreateView):
    form_class = UserCreationFormCustom
    template_name = "create.html"
    success_url = reverse_lazy("login")
    # extra_context = {'title': _('Registration user'), }
    extra_context = {'title': 'Регистрация пользователя',
                     'btn_name': 'Зарегистрировать',
                     }

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect("users")


class UpdateUser(UserPermissionsMixin, UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "update.html"
    login_url = "login"
    success_url = reverse_lazy("login")
    # extra_context = {'title': _('Update user'), }
    extra_context = {'title': 'Изменение пользователя',
                     'btn_name': 'Изменить',
                     }
    # permission_required = ('task_manager.view_user',
    #                        'task_manager.change_user'
    #                        )


class DeleteUser(UserPermissionsMixin, DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users")
    # extra_context = {'title': _('Delete user'), }
    extra_context = {'title': 'Удаление пользователя',
                     'btn_name': 'Да, удалить',
                     }
    # permission_required = ('task_manager.view_user',
    #                        'task_manager.delete_user'
    #                        )


class LoginUser(LoginView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("users")
    # extra_context = {'title': _('Enter'), }
    extra_context = {'title': 'Вход',
                     'btn_name': 'Войти',
                     }

    def get_success_url(self):
        return reverse_lazy('home')


def logout_user(request):
    logout(request)
    return redirect('home')
