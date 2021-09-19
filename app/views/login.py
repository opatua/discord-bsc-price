from typing import Any

from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView

from app.forms import LoginForm
from src.services import DateService


class LoginView(FormView):
    template_name = 'app/login.html'
    form_class = LoginForm
    date_service = DateService()

    def post(self, request: HttpRequest, *args: str, **kwargs: Any) -> HttpResponse:
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)

        if not user:
            messages.error(request, 'Invalid login.')
            return HttpResponseRedirect(reverse_lazy('login'))

        login(self.request, user)
        return HttpResponseRedirect(reverse_lazy('dashboard'))
