from solcast.base import Base
from solcast.utils import generate_dict


class PvPowerEstimatedActuals(Base):
    end_point = 'world_pv_power/estimated_actuals'

    def __init__(self, latitude, longitude, capacity, *args, **kwargs):

        self.latitude = latitude
        self.longitude = longitude
        self.capacity = capacity
        self.tilt = kwargs.get('tilt')
        self.azimuth = kwargs.get('azimuth')
        self.install_date = kwargs.get('install_date')
        self.loss_factor = kwargs.get('loss_factor')
        self.hours = kwargs.get('hours')
        self.latest = kwargs.get('latest', False)
        self.estimated_actuals = None

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

        if self.latest:
            self.end_point = self.end_point + '/latest'

        self._request('get', *args, **kwargs)

        if self.ok:
            self.forecasts = generate_dict(self.content.get('estimated_actuals'))
