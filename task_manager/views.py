from django import forms
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm, \
    UsernameField
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView


class UsersList(ListView):
    model = User
    template_name = "users.html"
    context_object_name = "users"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Пользователи'
        return context


class CreateUser(CreateView):
    form_class = UserCreationForm
    # model = User
    # fields = ['username', 'first_name', 'last_name',
    #           'email', 'password']
    template_name = "create.html"
    success_url = reverse_lazy("login")
    extra_context = {'title': 'Регистрация пользователя', }
    # # first_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}), max_length=150, help_text='First name')
    # # last_name = forms.CharField(forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}), max_length=150, help_text='Last name')
    #
    # class Meta(UserCreationForm.Meta):
    #     model = User
    #     fields = UserCreationForm.Meta.fields + ('first_name', 'last_name')



class UpdateUser(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "update.html"
    success_url = reverse_lazy("login")
    extra_context = {'title': 'Изменение пользователя', }


class DeleteUser(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users")
    extra_context = {'title': 'Удаление пользователя', }


class LoginUser(LoginView):
    # model = User
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = reverse_lazy("home")
    extra_context = {'title': 'Вход', }


class LogoutUser(LogoutView):
    model = User
    form_class = AuthenticationForm
    success_url = reverse_lazy("home")
