from solcast.base import Base
from solcast.utils import generate_dict


class RadiationEstimatedActuals(Base):
    end_point = 'world_radiation/estimated_actuals'

    def __init__(self, latitude, longitude, *args, **kwargs):

        self.latitude = latitude
        self.longitude = longitude
        self.hours = kwargs.get('hours')
        self.latest = kwargs.get('latest', False)
        self.estimated_actuals = None

        self.params = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'hours': self.hours
        }

        if self.latest:
            self.end_point = self.end_point + '/latest'

        self._request('get', *args, **kwargs)

        if self.ok:
            self.forecasts = generate_dict(self.content.get('estimated_actuals'))
