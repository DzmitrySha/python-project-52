from django.contrib import messages
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)

from labels.models import Label
from labels.permissions import LabelLoginRequiredMixin
from tasks.models import Tasks


class LabelsList(LabelLoginRequiredMixin, ListView):
    model = Label
    template_name = "labels/labels.html"
    context_object_name = "labels"
    login_url = "login"
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
    context_object_name = "label"
    extra_context = {'title': _('Delete label'),
                     'btn_name': _('Yes, delete'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Label successfully deleted'))
        return reverse_lazy('labels')
        # messages.info(self.request, _('Невозможно удалить метку, потому что она используется'))

    # def form_valid(self, form):
    #     label = Label.objects.get()
    #     for task in Tasks.objects.all():
    #         if label in task.labels.all():
    #             messages.info(
    #                 self.request,
    #                 _('Невозможно удалить метку, потому что она используется')
    #             )
    #             return reverse_lazy('labels')
    #     return super().form_valid(form)
