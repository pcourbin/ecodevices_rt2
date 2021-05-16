import inspect
import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2

from ..device_ecodevicesrt2 import EcoDevicesRT2Device

_LOGGER = logging.getLogger(__name__)


class BinarySensor_EcoDevicesRT2(EcoDevicesRT2Device, BinarySensorEntity):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        self._available = True
        self._is_on = False

    @property
    def is_on(self) -> bool:
        try:
            self._is_on = self.get_status()
            self._available = True
        except Exception as e:
            _LOGGER.error(
                "Device data no retrieve %s: %s (%s)",
                self.name,
                e,
                inspect.iscoroutinefunction(object),
            )
            self._available = False
        return self._is_on

    def get_status(self, cached_ms: int = None) -> bool:
        pass
