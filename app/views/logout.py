from django.contrib.auth import logout
from django.urls import reverse_lazy
from django.views.generic import RedirectView


class LogoutView(RedirectView):
    url = reverse_lazy('login')

    def get(self, request, *args, **kwargs):
        logout(request)

        return super().get(request, *args, **kwargs)