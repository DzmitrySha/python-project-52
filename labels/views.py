from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from labels.models import Label
from labels.mixins import LabelLoginRequiredMixin


class LabelsList(LabelLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/labels.html"
    login_url = "login"
    context_object_name = "labels"
    extra_context = {'title': _('Labels'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateLabel(SuccessMessageMixin, LabelLoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = "labels/form.html"
    login_url = "login"
    success_message = _('Label successfully created')
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Create label'),
                     'btn_name': _('Create')
                     }


class UpdateLabel(SuccessMessageMixin, LabelLoginRequiredMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = "labels/form.html"
    login_url = "login"
    success_message = _('Label successfully updated')
    success_url = reverse_lazy('labels')
    extra_context = {'title': _('Update label'),
                     'btn_name': _('Update'),
                     }


class DeleteLabel(LabelLoginRequiredMixin, DeleteView):
    model = Label
    template_name = "labels/delete.html"
    login_url = "login"
    success_url = reverse_lazy('labels')
    context_object_name = "label"
    extra_context = {'title': _('Delete label'),
                     'btn_name': _('Yes, delete'),
                     }

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.info(self.request, _('Label successfully deleted'))
        except ProtectedError:
            messages.error(
                self.request,
                _('It`s not possible to delete the label that is being used')
            )
        return redirect(success_url)
