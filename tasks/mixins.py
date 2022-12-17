from django.contrib import messages
from django.contrib.auth.mixins import (LoginRequiredMixin,
                                        PermissionRequiredMixin
                                        )
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class TasksLoginRequiredMixin(LoginRequiredMixin):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            messages.info(
                request,
                _('You are not logged in. Please log in.')
            )
            return self.handle_no_permission()
        return super().dispatch(request, *args, **kwargs)


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
