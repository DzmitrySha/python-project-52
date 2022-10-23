from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# from django.utils.translation import gettext_lazy as _


class UserCreationFormCustom(UserCreationForm):
    first_name = forms.CharField(
        # label=_("First name"),
        label="Имя",
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'false',
                                      }),
        # help_text=_("Enter user first name.")
        help_text="Введите Ваше имя."
    )

    last_name = forms.CharField(
        # label=_("Last name"),
        label="Фамилия",
        widget=forms.TextInput(attrs={'class': 'form-control',
                                      'type': 'text',
                                      'required': 'false',
                                      }),
        # help_text=_("Enter user last name.")
        help_text="Введите Вашу фамилию."
    )

    class Meta:
        model = User
        fields = UserCreationForm.Meta.fields + ('username',
                                                 'first_name', 'last_name')
