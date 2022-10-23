from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from task_manager.forms import UserCreationFormCustom


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


class UpdateUser(UpdateView):
    model = User
    # form_class =
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "update.html"
    success_url = reverse_lazy("login")
    # extra_context = {'title': _('Update user'), }
    extra_context = {'title': 'Изменение пользователя',
                     'btn_name': 'Изменить',
                     }


class DeleteUser(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users")
    # extra_context = {'title': _('Delete user'), }
    extra_context = {'title': 'Удаление пользователя', }


class LoginUser(LoginView):
    # model = User
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("users")
    # extra_context = {'title': _('Enter'), }
    extra_context = {'title': 'Вход',
                     'btn_name': 'Войти',
                     }


class LogoutUser(LogoutView):
    model = User
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
