from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, CreateView, DeleteView
from django.utils.translation import gettext_lazy as _

from groups.mixins import CanGroupDeletePermission
from groups.models import Group
from task_manager.mixins import AppLoginRequiredMixin


class GroupsList(AppLoginRequiredMixin, ListView):
    model = Group
    template_name = "groups/groups.html"
    context_object_name = "groups"
    extra_context = {'title': _('Groups'),
                     'btn_update': _('Update'),
                     'btn_delete': _('Delete'),
                     }


class CreateGroup(SuccessMessageMixin, AppLoginRequiredMixin, CreateView):
    model = Group
    fields = ['name', 'description', 'participants']
    template_name = "groups/form.html"
    success_message = _('Group successfully created')
    success_url = reverse_lazy('groups')
    extra_context = {'title': _('Create group'),
                     'btn_name': _('Create')
                     }

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class UpdateGroup(SuccessMessageMixin, AppLoginRequiredMixin, UpdateView):
    model = Group
    fields = ['name', 'description', 'participants']
    template_name = "groups/form.html"
    success_message = _('Group successfully updated')
    success_url = reverse_lazy('groups')
    extra_context = {'title': _('Update group'),
                     'btn_name': _('Update'),
                     }


class DeleteGroup(CanGroupDeletePermission,
                  AppLoginRequiredMixin,
                  SuccessMessageMixin,
                  DeleteView):
    model = Group
    template_name = "groups/delete.html"
    context_object_name = "group"
    success_message = _('Group successfully deleted')
    success_url = reverse_lazy('groups')
    extra_context = {'title': _('Delete group'),
                     'btn_name': _('Yes, delete'),
                     }
    permission_required = 'groups.creator'
