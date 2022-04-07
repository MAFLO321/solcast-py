from solcast.base import Base
from solcast.utils import generate_dict


class UtilityScaleSitesRadiationForecasts(Base):
    end_point = 'utility_scale_sites/{}/weather/forecasts'

    def __init__(self, resource_id, *args, **kwargs):

        self.end_point = self.end_point.format(resource_id)

        self.period = kwargs.get('period')
        self.hours = kwargs.get('hours')
        self.forecasts = None

        self.params = {
            'period': self.period,
            'hours': self.hours
        }

        self._request('get', *args, **kwargs)

        if self.ok:
            self.forecasts = generate_dict(self.content.get('forecasts'))
