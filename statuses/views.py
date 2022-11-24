from django.contrib import messages
from django.db.models import ProtectedError
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView, CreateView, UpdateView, DeleteView)
from statuses.models import TaskStatus
from statuses.permissions import StatusLoginRequiredMixin


class StatusesList(StatusLoginRequiredMixin, ListView):
    model = TaskStatus
    template_name = "statuses/statuses.html"
    context_object_name = "statuses"
    login_url = "login"
    extra_context = {'title': _('Statuses'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateStatus(StatusLoginRequiredMixin, CreateView):
    model = TaskStatus
    fields = ['name']
    template_name = "statuses/form.html"
    login_url = "login"
    extra_context = {'title': _('Create status'),
                     'btn_name': _('Create')
                     }

    def get_success_url(self):
        messages.info(self.request, _('Status successfully created'))
        return reverse_lazy('statuses')


class UpdateStatus(StatusLoginRequiredMixin, UpdateView):
    model = TaskStatus
    fields = ['name']
    template_name = "statuses/form.html"
    login_url = "login"
    extra_context = {'title': _('Update status'),
                     'btn_name': _('Update'),
                     }

    def get_success_url(self):
        messages.info(self.request, _('Status successfully updated'))
        return reverse_lazy('statuses')


class DeleteStatus(StatusLoginRequiredMixin, DeleteView):
    model = TaskStatus
    template_name = "statuses/delete.html"
    login_url = "login"
    success_url = reverse_lazy('statuses')
    context_object_name = "status"
    extra_context = {'title': _('Delete status'),
                     'btn_name': _('Yes, delete'),
                     }

    def form_valid(self, form):
        success_url = self.get_success_url()
        try:
            self.object.delete()
            messages.info(self.request, _('Status successfully deleted'))
        except ProtectedError:
            messages.error(
                self.request,
                _('It`s not possible to delete the status that is being used')
            )
        return redirect(success_url)
