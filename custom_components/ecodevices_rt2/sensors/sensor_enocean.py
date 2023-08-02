from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import EnOceanSensor

from . import Sensor_EcoDevicesRT2


class Sensor_EnOcean(Sensor_EcoDevicesRT2):
    """Representation of an EnOcean sensor."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(hass, device_config, ecort2, coordinator)
        self.control = EnOceanSensor(ecort2, self._id)

    def get_property(self, cached_ms: int = None):
        value = self.control.get_value(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
