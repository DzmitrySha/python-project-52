from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView


class UsersList(ListView):
    model = User
    template_name = "users.html"
    context_object_name = "users"

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

# def get_users(request):
#     users = User.objects.all()
#     return render(request,
#                   template_name="users.html",
#                   context={
#                       "title": "Пользователи",
#                       "users": users,
#                   })


class CreateUser(CreateView):
    form_class = UserCreationForm
    template_name = "create.html"
    success_url = reverse_lazy("login")


# def create_user(request):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     return render(request,
#                   template_name="create.html",
#                   context={
#                       "form": form_class,
#                       "title": "Регистрация",
#                   })
