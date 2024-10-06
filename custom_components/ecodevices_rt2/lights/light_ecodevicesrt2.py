import inspect
import logging

from homeassistant.components.light import ColorMode
from homeassistant.components.light import LightEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2

from ..device_ecodevicesrt2 import EcoDevicesRT2Device

_LOGGER = logging.getLogger(__name__)


class Light_EcoDevicesRT2(EcoDevicesRT2Device, LightEntity):
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
        self._attr_supported_color_modes = {ColorMode.ONOFF}
        self._attr_color_mode = ColorMode.ONOFF

    @property
    def is_on(self) -> bool:
        """Return true if switch is on. Standby is on."""
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

    @property
    def available(self):
        """Return true if switch is available."""
        return True
        # return self._available

    async def async_turn_on(self, **kwargs):
        """Turn the switch on at next update."""
        try:
            if await self.hass.async_add_executor_job(self.set_on):
                self._available = True
                await self.coordinator.async_request_refresh()
            else:
                _LOGGER.warning("Error while turning on device %s", self._name)
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False

    async def async_turn_off(self, **kwargs):
        """Turn the switch on at next update."""
        try:
            if await self.hass.async_add_executor_job(self.set_off):
                self._available = True
                await self.coordinator.async_request_refresh()
            else:
                _LOGGER.warning("Error while turning on device %s", self._name)
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False

    def get_status(self, cached_ms: int = None) -> bool:
        pass

    def set_on(self) -> bool:
        pass

    def set_off(self) -> bool:
        pass
