from django.conf.urls import include, url
from django.urls import path

from app import views


urlpatterns = [
    path('', views.LoginView.as_view(), name='login'),
    path('change-password', views.ChangePasswordView.as_view(), name='change_password'),
    path('dashboard', views.DashboardView.as_view(), name='dashboard'),
    path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.LogoutView.as_view(), name='logout'),
    path('hello', views.HelloView.as_view(), name='hello'),

    path('user/data', views.UserDataView.as_view(), name='user_data'),
    path('user', views.UserListView.as_view(), name='user_list'),
    path('user/create', views.UserCreateView.as_view(), name='user_create'),
    path('user/<slug:pk>/update', views.UserUpdateView.as_view(), name='user_update'),
    path('user/<slug:pk>/password', views.UserPasswordChangeView.as_view(), name='user_password'),
    path('user/<slug:pk>/delete', views.UserDeleteView.as_view(), name='user_delete'),
]
