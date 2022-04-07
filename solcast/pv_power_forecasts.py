from solcast.base import Base
from solcast.utils import generate_dict


class PvPowerForecasts(Base):
    end_point = 'world_pv_power/forecasts'

    def __init__(self, latitude, longitude, capacity, *args, **kwargs):

        self.latitude = latitude
        self.longitude = longitude
        self.capacity = capacity
        self.tilt = kwargs.get('tilt')
        self.azimuth = kwargs.get('azimuth')
        self.install_date = kwargs.get('install_date')
        self.loss_factor = kwargs.get('loss_factor')
        self.hours = kwargs.get('hours')
        self.forecasts = None

        self.params = {
            'latitude': self.latitude,
            'longitude': self.longitude,
            'capacity': self.capacity,
            'tilt': self.tilt,
            'azimuth': self.azimuth,
            'install_date': self.install_date,
            'loss_factor': self.loss_factor,
            'hours': self.hours
        }

        self._request('get', *args, **kwargs)

        if self.ok:
            self.forecasts = generate_dict(self.content.get('forecasts'))
