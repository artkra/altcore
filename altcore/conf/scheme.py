from __future__ import absolute_import

from django.db import models


SCHEME = {
    'EntityOne': {
        'features': [
            {
                'name': 'FeatureOne',
                'type': models.BooleanField('self')
            }
        ],
        'links': [
            {
                'name': 'LinkOne',
                'linked_with': 'EntityTwo'
            }
        ],
        'routes': 'entity_one'
    }
}