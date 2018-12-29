from __future__ import absolute_import

from django.db import models

from common.configuration import configure


_core_attrs = {
    'entity_name': models.CharField(max_length=100, verbose_name='Main entity name'),
    'entity_type': models.CharField(max_length=100, verbose_name='Main entity type'),
    '__module__': 'main.models'
}

attrs = configure(_core_attrs)

Root = type(
    'Root',
    (models.Model,),
    attrs
)
