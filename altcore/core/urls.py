from __future__ import absolute_import

from django.conf.urls import url, include
from rest_framework import routers

from common.router import register_root

router = routers.DefaultRouter()

router = register_root(router)

urlpatterns = [
    url(r'^api/', include(router.urls)),
]
