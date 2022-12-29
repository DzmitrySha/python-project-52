from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class CanTaskDeletePermission(PermissionRequiredMixin):
    def has_permission(self):
        return self.get_object().author == self.request.user

    def handle_no_permission(self):
        messages.error(
            self.request, _('A task can only be deleted by its author')
        )
        return redirect('tasks')
