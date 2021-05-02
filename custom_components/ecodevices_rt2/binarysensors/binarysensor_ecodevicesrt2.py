import logging

from homeassistant.components.binary_sensor import BinarySensorEntity
from pyecodevices_rt2 import EcoDevicesRT2

from .. import EcoDevicesRT2Device

_LOGGER = logging.getLogger(__name__)


class BinarySensor_EcoDevicesRT2(EcoDevicesRT2Device, BinarySensorEntity):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self._available = True
        self._is_on = False

    @property
    def is_on(self) -> bool:
        """Return true if switch is on. Standby is on."""
        return self._is_on

    def _async_get_status(self) -> bool:
        pass

    async def async_update(self):

        try:
            self._is_on = await self.hass.async_add_executor_job(self._async_get_status)
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False
