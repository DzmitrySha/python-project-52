from django import forms
# from django.contrib.auth.models import User

from tasks.models import Tasks
# from django.db.models.functions import Concat
# from django.db.models import Value
# from django.utils.translation import gettext_lazy as _


class TaskUpdateForm(forms.ModelForm):
    # executors = User.objects.exclude(first_name='', last_name='').values_list(
    #     Concat('first_name', Value(' '), 'last_name')
    # )
    #
    # executor = forms.ModelChoiceField(
    #     label=_('Executor'),
    #     queryset=executors
    # )

    class Meta:
        model = Tasks
        fields = ['name', 'description', 'status', 'executor', 'labels']
