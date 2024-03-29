from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2

from . import Sensor_EcoDevicesRT2


class Sensor_API(Sensor_EcoDevicesRT2):
    """Representation of an API sensor."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        get,
        get_value,
        get_entry,
    ):
        super().__init__(hass, device_config, ecort2, coordinator)
        self._get = get
        self._get_value = get_value
        self._get_entry = get_entry

        # Add Call to cached value in ecort2
        ecort2._cached[self._get + "=" + self._get_value] = {}

    def get_property(self, cached_ms: int = None):
        value = self.ecort2.get(
            self._get, self._get_value, self._get_entry, cached_ms=cached_ms
        )
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
