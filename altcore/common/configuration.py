from __future__ import absolute_import

from django.db import models

from conf import scheme


def configure(attrs_dict):
    entities = {}
    fields = {}

    for entitie, items in scheme.SCHEME.items():
        entities[entitie.lower()] = models.ManyToManyField('self')
        for feature in items['features']:
            fields[feature['name'].lower()] = feature['type']

    attrs_dict.update(**fields)
    attrs_dict.update(**entities)
    attrs_dict['__module__'] = 'main.models'

    return attrs_dict
