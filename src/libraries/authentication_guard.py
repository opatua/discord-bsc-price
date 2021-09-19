from django.http import HttpResponseRedirect
from django.urls import reverse_lazy


class AuthGuard():

    def dispatch(self, request, *args, **kwargs):

        if not request.user:
            return HttpResponseRedirect(reverse_lazy('login'))

        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse_lazy('login'))

        return super(AuthGuard, self).dispatch(request, *args, **kwargs)