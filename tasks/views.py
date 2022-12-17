from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import (DetailView, CreateView,
                                  UpdateView, DeleteView,
                                  )
from django_filters.views import FilterView
from django.utils.translation import gettext_lazy as _

from tasks.filters import TaskFilterForm
from tasks.permissions import (TasksLoginRequiredMixin,
                               CanTaskDeletePermission
                               )
from tasks.models import Tasks


class TasksList(TasksLoginRequiredMixin, FilterView):
    model = Tasks
    filterset_class = TaskFilterForm
    template_name = "tasks/tasks.html"
    context_object_name = "tasks"
    login_url = 'login'
    extra_context = {'title': _('Tasks'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     'btn_show': _('Show'),
                     }


class TaskDetailView(SuccessMessageMixin, TasksLoginRequiredMixin, DetailView):
    model = Tasks
    template_name = "tasks/task.html"
    context_object_name = "task"
    login_url = 'login'
    extra_context = {'title': _('Task view'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateTask(SuccessMessageMixin, TasksLoginRequiredMixin, CreateView):
    model = Tasks
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/form.html"
    login_url = "login"
    success_message = _('Task successfully created')
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Create task'),
                     'btn_name': _('Create')
                     }

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class UpdateTask(SuccessMessageMixin, TasksLoginRequiredMixin, UpdateView):
    model = Tasks
    fields = ['name', 'description', 'status', 'executor', 'labels']
    template_name = "tasks/form.html"
    login_url = "login"
    success_message = _('Task successfully updated')
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Update task'),
                     'btn_name': _('Update'),
                     }


class DeleteTask(TasksLoginRequiredMixin,
                 CanTaskDeletePermission,
                 DeleteView):
    model = Tasks
    template_name = "tasks/delete.html"
    login_url = "login"
    context_object_name = "task"
    success_message = _('Task successfully deleted')
    success_url = reverse_lazy('tasks')
    extra_context = {'title': _('Delete task'),
                     'btn_name': _('Yes, delete'),
                     }
    permission_required = 'tasks.author'
