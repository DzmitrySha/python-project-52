from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from labels.models import TaskLabels
from task_manager.mixins import AppLoginRequiredMixin


class LabelsList(AppLoginRequiredMixin, ListView):
    model = TaskLabels
    template_name = "labels/labels.html"
    context_object_name = "labels"
    extra_context = {'title': _('Labels'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateLabel(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = TaskLabels
    fields = ['name']
    template_name = "labels/form.html"
    success_message = _('Label successfully created')
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Create label'),
                     'btn_name': _('Create')
                     }


class UpdateLabel(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = TaskLabels
    fields = ['name']
    template_name = "labels/form.html"
    success_message = _('Label successfully updated')
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Update label'),
                     'btn_name': _('Update'),
                     }


class DeleteLabel(SuccessMessageMixin, AppLoginRequiredMixin, DeleteView):
    model = TaskLabels
    template_name = "labels/delete.html"
    success_url = reverse_lazy('labels')
    success_message = _('Label successfully deleted')
    context_object_name = "label"
    extra_context = {'title': _('Delete label'),
                     'btn_name': _('Yes, delete'),
                     }

    def post(self, request, *args, **kwargs):
        if self.get_object().labels.count():
            messages.error(
                self.request,
                _('It`s not possible to delete the label that is being used')
            )
            return redirect(self.success_url)
        return super().post(request, *args, **kwargs)
