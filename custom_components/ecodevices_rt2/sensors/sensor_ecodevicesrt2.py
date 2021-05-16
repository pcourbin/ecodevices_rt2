import logging

from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2

from ..device_ecodevicesrt2 import EcoDevicesRT2Device

_LOGGER = logging.getLogger(__name__)


class Sensor_EcoDevicesRT2(EcoDevicesRT2Device, Entity):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        self._state = None

    @property
    def state(self) -> str:
        """Return the state."""
        try:
            self._state = self.get_property()
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False
        return self._state

    def get_property(self, cached_ms: int = None) -> bool:
        pass
