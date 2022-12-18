from django.contrib import messages
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class CanTaskDeletePermission(PermissionRequiredMixin):
    def has_permission(self):
        return self.get_object().author == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            messages.error(
                request,
                _('A task can only be deleted by its author')
            )
            return redirect('tasks')
        return super().dispatch(request, *args, **kwargs)