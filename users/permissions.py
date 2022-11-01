from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserPermissionsMixin:
    def has_permissions(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permissions():
            if not request.user.is_authenticated:
                messages.info(
                    request,
                    _('You are not logged in. Please log in.')
                )
                return redirect('login')
            else:
                messages.error(
                    request,
                    _('You don\'t have the rights to change another user.')
                )
                return redirect('users')
        return super().dispatch(request, *args, **kwargs)
