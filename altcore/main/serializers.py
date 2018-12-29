from __future__ import absolute_import

from rest_framework import serializers

from main.models import Root


class RootSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Root
        fields = ('id', 'entity_name', 'entity_type', 'FeatureOne', 'EntityOne')
