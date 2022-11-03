from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (
    ListView, DetailView, CreateView, UpdateView, DeleteView
)
from django.utils.translation import gettext_lazy as _
from tasks.permissions import TasksLoginRequiredMixin
from tasks.models import Tasks


class TasksList(TasksLoginRequiredMixin, ListView):
    model = Tasks
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    login_url = 'login'
    extra_context = {'title': _('Tasks'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class OneTaskView(TasksLoginRequiredMixin, DetailView):
    model = Tasks
    template_name = "tasks/task.html"
    context_object_name = "task"
    login_url = 'login'
    extra_context = {'title': _('Task view'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateTask(TasksLoginRequiredMixin, CreateView):
    model = Tasks
    fields = ['name', 'description', 'status', 'author', 'executor']
    template_name = "tasks/form.html"
    login_url = "login"
    extra_context = {'title': _('Create task'),
                     'btn_name': _('Create')
                     }

    def get_success_url(self):
        messages.info(self.request, _('Task successfully created'))
        return reverse_lazy('tasks')


class UpdateTask(TasksLoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['name', 'description', 'status', 'author', 'executor']
    template_name = "tasks/form.html"
    login_url = "login"
    extra_context = {'title': _('Update task'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Task successfully updated'))
        return reverse_lazy('tasks')


class DeleteTask(TasksLoginRequiredMixin, DeleteView):
    model = Tasks
    template_name = "tasks/delete.html"
    login_url = "login"
    extra_context = {'title': _('Delete task'),
                     'btn_name': _('Yes, delete'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Task successfully deleted'))
        return reverse_lazy('tasks')
