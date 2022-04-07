from solcast.base import Base
from solcast.utils import generate_dict


class UtilityScaleSitesPvPowerEstimatedActuals(Base):
    end_point = 'utility_scale_sites/{}/estimated_actuals'

    def __init__(self, resource_id, *args, **kwargs):

        self.end_point = self.end_point.format(resource_id)

        self.period = kwargs.get('period')
        self.hours = kwargs.get('hours')
        self.apply_availability = kwargs.get('apply_availability')
        self.apply_constraint = kwargs.get('apply_constraint')
        self.apply_dust_soiling = kwargs.get('apply_dust_soiling')
        self.apply_snow_soiling = kwargs.get('apply_snow_soiling')
        self.apply_tracker_inactive = kwargs.get('apply_tracker_inactive')
        self.estimated_actuals = None

        self.params = {
            'period': self.period,
            'hours': self.hours,
            'apply_availability': self.apply_availability,
            'apply_constraint': self.apply_constraint,
            'apply_dust_soiling': self.apply_dust_soiling,
            'apply_snow_soiling': self.apply_snow_soiling,
            'apply_tracker_inactive': self.apply_tracker_inactive
        }

        self._request('get', *args, **kwargs)

        if self.ok:
            self.estimated_actuals = generate_dict(self.content.get('estimated_actuals'))
