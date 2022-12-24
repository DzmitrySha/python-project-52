from django import forms
from django_filters import FilterSet, ModelChoiceFilter, BooleanFilter
from django.utils.translation import gettext_lazy as _

from labels.models import TaskLabels
from tasks.models import Task


class TaskFilterForm(FilterSet):
    labels = ModelChoiceFilter(label=_('Label'),
                               queryset=TaskLabels.objects.all())
    user_tasks_only = BooleanFilter(label=_('Only self tasks'),
                                    widget=forms.CheckboxInput(),
                                    method='filter_self_tasks',
                                    field_name='only_self_tasks'
                                    )

    def filter_self_tasks(self, queryset, name, value):
        lookup = queryset.filter(author=self.request.user)
        return lookup if value else queryset

    class Meta:
        model = Task
        fields = ['status', 'executor', 'labels']
