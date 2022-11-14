from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
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

#
# class TasksPermissionRequiredMixin:
#     def has_permissions(self):
#         return self.get_object().author_id == self.request.user
#
#     def dispatch(self, request, *args, **kwargs):
#         if not self.has_permissions():
#             messages.info(
#                 request,
#                 _('You are not have permissions.')
#             )
#             return self.handle_no_permission()
#         return super().dispatch(request, *args, **kwargs)