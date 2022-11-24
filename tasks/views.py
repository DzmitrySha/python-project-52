from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView
                                  )
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

from tasks.permissions import (TasksLoginRequiredMixin,
                               TasksPermissionRequiredMixin
                               )
from tasks.models import Tasks


class TasksList(TasksLoginRequiredMixin, FilterView):
    model = Tasks
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    login_url = 'login'
    extra_context = {'title': _('Tasks'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     'btn_show': _('Show'),
                     }
    filterset_fields = ['status', 'executor', 'labels', 'author']


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
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/form.html"
    login_url = "login"
    extra_context = {'title': _('Create task'),
                     'btn_name': _('Create')
                     }

    def get_success_url(self):
        messages.info(self.request, _('Task successfully created'))
        return reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(TasksLoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/form.html"
    login_url = "login"
    extra_context = {'title': _('Update task'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Task successfully updated'))
        return reverse_lazy('tasks')


class DeleteTask(TasksLoginRequiredMixin,
                 TasksPermissionRequiredMixin,
                 DeleteView):
    model = Tasks
    template_name = "tasks/delete.html"
    login_url = "login"
    context_object_name = "task"
    extra_context = {'title': _('Delete task'),
                     'btn_name': _('Yes, delete'),
                     }
    permission_required = 'tasks.author'

    def get_success_url(self):
        messages.info(self.request, _('Task successfully deleted'))
        return reverse_lazy('tasks')
