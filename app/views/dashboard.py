from django.views.generic import TemplateView

from src.libraries import AuthGuard


class DashboardView(AuthGuard, TemplateView):
    template_name = 'app/dashboard.html'