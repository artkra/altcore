from __future__ import absolute_import

from rest_framework import viewsets

from main.models import Root
from main.serializers import RootSerializer


class RootViewSet(viewsets.ModelViewSet):
    queryset = Root.objects.all().order_by('id')
    serializer_class = RootSerializer
