from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from labels.models import Label
from labels.permissions import LabelLoginRequiredMixin


class LabelsList(LabelLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/labels.html"
    login_url = "login"
    context_object_name = "labels"
    extra_context = {'title': _('Labels'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateLabel(LabelLoginRequiredMixin, CreateView):
    model = Label
    fields = ['name']
    template_name = "labels/form.html"
    login_url = "login"
    extra_context = {'title': _('Create label'),
                     'btn_name': _('Create')
                     }

    def get_success_url(self):
        messages.info(self.request, _('Label successfully created'))
        return reverse_lazy('labels')


class UpdateLabel(LabelLoginRequiredMixin, UpdateView):
    model = Label
    fields = ['name']
    template_name = "labels/form.html"
    login_url = "login"
    extra_context = {'title': _('Update label'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Label successfully updated'))
        return reverse_lazy('labels')


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
