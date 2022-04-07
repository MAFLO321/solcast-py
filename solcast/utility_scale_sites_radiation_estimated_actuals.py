from solcast.base import Base
from solcast.utils import generate_dict


class UtilityScaleSitesRadiationEstimatedActuals(Base):
    end_point = 'utility_scale_sites/{}/weather/estimated_actuals'

    def __init__(self, resource_id, *args, **kwargs):

        self.end_point = self.end_point.format(resource_id)

        self.period = kwargs.get('period')
        self.hours = kwargs.get('hours')
        self.estimated_actuals = None

        self.params = {
            'period': self.period,
            'hours': self.hours
        }

        self._request('get', *args, **kwargs)

        if self.ok:
            self.estimated_actuals = generate_dict(self.content.get('estimated_actuals'))
