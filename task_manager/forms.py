from django.forms import ModelForm
from django.contrib.auth.models import User


class LoginForm(ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class UpdateForm(LoginForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'password']
