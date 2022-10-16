# from django.shortcuts import render
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
    model = User
    fields = ['username', 'first_name', 'last_name',
              'email', 'password']
    template_name = "create.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Регистрация пользователя'
        return context


class UpdateUser(UpdateView):
    model = User
    fields = ['username', 'first_name', 'last_name', 'email', 'password']
    template_name = "update.html"
    success_url = reverse_lazy("login")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Изменение пользователя'
        return context


class DeleteUser(DeleteView):
    model = User
    template_name = "delete.html"
    success_url = reverse_lazy("users")
    extra_context = {'title': 'Удаление пользователя', }


class LoginUser(LoginView):
    model = User
    template_name = "login.html"
    success_url = reverse_lazy("home")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Страница входа'
        return context


# class LogoutUser(LogoutView):
#     model = User
#     template_name = "logout.html"
#     success_url = reverse_lazy("home")
