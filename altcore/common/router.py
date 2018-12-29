from __future__ import absolute_import

from rest_framework import routers

from main import views

router = routers.DefaultRouter()


def register_root(router):
    router.register(r'root', views.RootViewSet)
    return router
