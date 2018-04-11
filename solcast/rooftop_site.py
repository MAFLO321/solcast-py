import json

from solcast.base import Base
from solcast.utils import DictNoNone


class RooftopSite(Base):
    end_point = 'rooftop_sites'

    def __init__(self, name, latitude, longitude, *args, **kwargs):

        self.name = name
        self.latitude = latitude
        self.longitude = longitude

        self.site = None
        self.params = {}

        payload = DictNoNone(name=self.name, latitude=self.latitude, longitude=self.longitude)
        payload['install_date'] = kwargs.get('install_date', None)
        payload['tags'] = kwargs.get('tags', None)
        payload['azimuth'] = kwargs.get('azimuth', None)
        payload['tilt'] = kwargs.get('tilt', None)
        payload['loss_factor'] = kwargs.get('loss_factor', None)

        data = '{{ "site":{} }}'.format(json.dumps(payload, default=lambda a: a.__dict__))

        self._request('post', data=data, headers={"Content-Type": "application/json"}, *args, **kwargs)

        if self.ok:
            self.site = self.content['site']

