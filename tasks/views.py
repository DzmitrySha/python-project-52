from django.shortcuts import render
from django.views.generic import ListView
from django.utils.translation import gettext_lazy as _

from tasks.permissions import TasksLoginRequiredMixin
from tasks.models import Tasks


# Create your views here.

class TasksList(TasksLoginRequiredMixin, ListView):
    model = Tasks
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    extra_context = {'title': _('Tasks'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


# class OneTaskList(DetailView):
