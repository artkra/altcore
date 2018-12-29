from __future__ import absolute_import

from rest_framework import viewsets

from main.models import Root
from main.serializers import RootSerializer


class RootViewSet(viewsets.ModelViewSet):
    queryset = Root.objects.all().order_by('id')
    serializer_class = RootSerializer


def generate_viewset(entity_type):
    return type(
            '{}ViewSet'.format(entity_type),
            (viewsets.ModelViewSet),
            {
                'queryset': Root.objects.filter(entity_type=entity_type).order_by('id'),
                'serializer_class': RootSerializer
            }
        )
