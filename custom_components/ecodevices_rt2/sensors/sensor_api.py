from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2

from . import Sensor_EcoDevicesRT2


class Sensor_API(Sensor_EcoDevicesRT2, Entity):
    """Representation of an EnOcean sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        get,
        get_value,
        get_entry,
    ):
        super().__init__(device_config, ecort2)
        self._get = get
        self._get_value = get_value
        self._get_entry = get_entry

    def _async_get_property(self):
        return self.ecort2.get(self._get, self._get_value, self._get_entry)
