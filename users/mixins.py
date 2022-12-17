from django.contrib import messages
from django.contrib.auth.mixins import UserPassesTestMixin
from django.shortcuts import redirect
from django.utils.translation import gettext_lazy as _


class UserPermissionsMixin(UserPassesTestMixin):

    def test_func(self):
        return self.get_object() == self.request.user

    def dispatch(self, request, *args, **kwargs):
        if not self.get_test_func()():
            if not request.user.is_authenticated:
                messages.error(
                    request,
                    _('You are not logged in. Please log in.'))
                return redirect('login')
            else:
                messages.error(
                    request,
                    _('You don\'t have the rights to change another user.'))
                return redirect('users')
        return super().dispatch(request, *args, **kwargs)
