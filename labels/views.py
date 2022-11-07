from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from labels.models import Labels
from labels.permissions import LabelLoginRequiredMixin


class LabelsList(LabelLoginRequiredMixin, ListView):
    model = Labels
    template_name = "labels/labels.html"
    context_object_name = "labels"
    login_url = "login"
    extra_context = {'title': _('Labels'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateLabel(LabelLoginRequiredMixin, CreateView):
    model = Labels
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
    model = Labels
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
    model = Labels
    template_name = "labels/delete.html"
    login_url = "login"
    context_object_name = "label"
    extra_context = {'title': _('Delete label'),
                     'btn_name': _('Yes, delete'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Label successfully deleted'))
        return reverse_lazy('labels')
