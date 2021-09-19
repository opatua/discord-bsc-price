from django.db.models import Q
from django.template.loader import render_to_string
from django.urls import reverse_lazy
from django.views.generic import TemplateView, UpdateView, DeleteView, CreateView

from django_datatables_view.base_datatable_view import BaseDatatableView

from src.models import User
from app.forms import UserForm, UserPasswordChangeForm, UserProfileEditForm
from src.libraries import AuthGuard


class UserDataView(AuthGuard, BaseDatatableView):
    model = User
    columns = [
        'email',
        'name',
        'is_active',
        'action',
    ]

    def render_column(self, row, column):
        if column == 'action':
            return render_to_string(
                'app/snippets/action.html', {
                    'password_link': reverse_lazy('user_password', kwargs={'pk': row.id}),
                    'update_link': reverse_lazy('user_update', kwargs={'pk': row.id}),
                    'delete_link': reverse_lazy('user_delete', kwargs={'pk': row.id}),
                },
            )

        return super().render_column(row, column)

    def filter_queryset(self, qs):
        search = self.request.GET.get('search[value]', None)
        if search:
            qs = qs.filter(
                Q(id__icontains=search) |
                Q(email__icontains=search) |
                Q(name__icontains=search)
            )

        return qs


class UserListView(AuthGuard, TemplateView):
    template_name = 'app/user/index.html'


class UserCreateView(AuthGuard, CreateView):
    model = User
    template_name = 'app/user/create.html'
    form_class = UserForm
    success_url = reverse_lazy('user_index')


class UserUpdateView(AuthGuard, UpdateView):
    model = User
    template_name = 'app/user/update.html'
    form_class = UserProfileEditForm
    success_url = reverse_lazy('user_list')


class UserDeleteView(AuthGuard, DeleteView):
    model = User
    template_name = 'app/user/delete.html'
    success_url = reverse_lazy('user_list')


class UserPasswordChangeView(AuthGuard, UpdateView):
    model = User
    template_name = 'app/user/change_password.html'
    form_class = UserPasswordChangeForm
    success_url = reverse_lazy('user_list')

    def get_initial(self):
        initial = super().get_initial()
        initial['password'] = ''

        return initial
