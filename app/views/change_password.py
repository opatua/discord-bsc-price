from django.contrib.auth import update_session_auth_hash
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView

from app.forms import PasswordChangeForm
from src.libraries import AuthGuard


class ChangePasswordView(AuthGuard, TemplateView):
    template_name = 'app/change_password.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(
            user=request.user,
            data=request.POST
        )
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return HttpResponseRedirect(reverse_lazy('change_password'))

        return HttpResponseRedirect(reverse_lazy('change_password'))
