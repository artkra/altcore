from __future__ import absolute_import

from rest_framework import serializers

from main.models import Root


class CustomRelatedField(serializers.RelatedField):
    def __init__(self, *args, **kwargs):
        super(CustomRelatedField, self).__init__(*args, **kwargs)

    def to_representation(self, value):
        return {'id': value.id, 'name': value.entity_name, 'type': value.entity_type}


class RootSerializer(serializers.HyperlinkedModelSerializer):
    entityone = CustomRelatedField(many=True, read_only=True)

    class Meta:
        model = Root
        fields = ('id', 'entity_name', 'entity_type', 'entityone')

    def create(self, validated_data):
        data = self.initial_data
        return Root.objects.first()
