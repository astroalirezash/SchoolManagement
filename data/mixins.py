from django.http import Http404
from django.shortcuts import redirect


class StudentsMixin:
    """
    This mixin redirects students to another page
    """
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_student:
            return redirect('')  # TODO: view name
        elif request.user.is_authenticated:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404