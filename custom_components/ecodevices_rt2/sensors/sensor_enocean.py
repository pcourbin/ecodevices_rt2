from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import EnOceanSensor

from . import Sensor_EcoDevicesRT2


class Sensor_EnOcean(Sensor_EcoDevicesRT2, Entity):
    """Representation of an EnOcean sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
    ):
        super().__init__(device_config, ecort2)
        self.control = EnOceanSensor(ecort2, self._id)

    def _async_get_property(self):
        return self.control.value
