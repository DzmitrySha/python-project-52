from django import forms
# from django.contrib.auth.models import User
from tasks.models import Tasks


class TaskUpdateForm(forms.ModelForm):
    # executor = forms.ModelChoiceField(
    #     label='Executor',
    #     queryset=User.objects.all().values_list('first_name', 'last_name')
    # )

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']
