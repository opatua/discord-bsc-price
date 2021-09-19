from django.conf.urls import include, url
from django.urls import path
from rest_framework.routers import DefaultRouter

from api import views


urlpatterns = [
    url(
        r'^api/(?P<version>(1))/',
        include(
            [
                path(
                    'hello',
                    views.HelloView.as_view(),
                    name='hello_api'
                ),
            ]
        )
    )

]
