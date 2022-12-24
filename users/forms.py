from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


class UserCreationFormCustom(UserCreationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['first_name'].required = True
        self.fields['last_name'].required = True

    class Meta:
        model = get_user_model()
        fields = ['username', 'first_name', 'last_name']
