from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView,
                                  )
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

from tasks.filters import TaskFilterForm
from task_manager.mixins import AppLoginRequiredMixin
from tasks.mixins import CanTaskDeletePermission
from tasks.models import Task


class TasksList(AppLoginRequiredMixin, FilterView):
    model = Task
    filterset_class = TaskFilterForm
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    extra_context = {'title': _('Tasks'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     'btn_show': _('Show'),
                     }


class TaskDetailView(SuccessMessageMixin, AppLoginRequiredMixin, DetailView):
    model = Task
    template_name = "tasks/task.html"
    context_object_name = "task"
    extra_context = {'title': _('Task view'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateTask(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/form.html"
    success_message = _('Task successfully created')
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Create task'),
                     'btn_name': _('Create')
                     }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = Task
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/form.html"
    success_message = _('Task successfully updated')
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Update task'),
                     'btn_name': _('Update'),
                     }


class DeleteTask(AppLoginRequiredMixin,
                 CanTaskDeletePermission,
                 SuccessMessageMixin,
                 DeleteView):
    model = Task
    template_name = "tasks/delete.html"
    context_object_name = "task"
    success_message = _('Task successfully deleted')
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Delete task'),
                     'btn_name': _('Yes, delete'),
                     }
    permission_required = 'tasks.author'
