from solcast.base import Base
from solcast.utils import generate_dict


class RadiationForecasts(Base):
    end_point = 'world_radiation/forecasts'

    def __init__(self, latitude, longitude, *args, **kwargs):

        self.latitude = latitude
        self.longitude = longitude
        self.hours = kwargs.get('hours')
        self.forecasts = None

        self.params = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'hours': self.hours
        }

        self._request('get', *args, **kwargs)

        if self.ok:
            self.forecasts = generate_dict(self.content.get('forecasts'))
