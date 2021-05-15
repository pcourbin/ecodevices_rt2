import asyncio
import logging

from homeassistant.components.switch import SwitchEntity
from pyecodevices_rt2 import EcoDevicesRT2

from ..device_ecodevicesrt2 import EcoDevicesRT2Device

_LOGGER = logging.getLogger(__name__)


class Switch_EcoDevicesRT2(EcoDevicesRT2Device, SwitchEntity):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self._available = True
        self._is_on = False
        self._is_on_command = self._is_on
        self._updated = True

    @property
    def is_on(self) -> bool:
        """Return true if switch is on. Standby is on."""
        return self._is_on

    @property
    def available(self):
        """Return true if switch is available."""
        return self._available

    def turn_on(self, **kwargs) -> None:
        """Turn the switch on at next update."""
        self._is_on_command = True
        self._updated = False
        self.schedule_update_ha_state()

    def turn_off(self, **kwargs) -> None:
        """Turn the switch off at next update."""
        self._is_on_command = False
        self._updated = False
        self.schedule_update_ha_state()

    async def async_toggle(self, **kwargs) -> None:
        """Toggle the switch."""
        self._is_on_command = not self._is_on_command
        self._updated = False
        self.schedule_update_ha_state()

    def _async_get_status(self, cached_ms: int = None) -> bool:
        pass

    def _async_set_on(self) -> bool:
        pass

    def _async_set_off(self) -> bool:
        pass

    async def async_update(self):

        try:
            self._is_on = await self.hass.async_add_executor_job(self._async_get_status)
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False

        if self._is_on_command != self._is_on:
            if self._updated is False:
                if self._is_on_command:
                    try:
                        if await self.hass.async_add_executor_job(self._async_set_on):
                            self._available = True
                            self._updated = True
                            await asyncio.sleep(1)
                            self._is_on = await self.hass.async_add_executor_job(
                                self._async_get_status, 0
                            )
                        else:
                            _LOGGER.warning(
                                "Error while turning on device %s", self._name
                            )
                    except Exception as e:
                        _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
                        self._available = False
                else:
                    try:
                        if await self.hass.async_add_executor_job(self._async_set_off):
                            self._available = True
                            self._updated = True
                            await asyncio.sleep(1)
                            self._is_on = await self.hass.async_add_executor_job(
                                self._async_get_status, 0
                            )
                        else:
                            _LOGGER.warning(
                                "Error while turning off device %s", self._name
                            )
                    except Exception as e:
                        _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
                        self._available = False
            else:
                self._is_on_command = self._is_on
