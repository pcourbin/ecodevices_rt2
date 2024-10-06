import inspect
import logging

from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate import ClimateEntityFeature
from homeassistant.components.climate import HVACMode
from homeassistant.components.climate import PRESET_AWAY
from homeassistant.components.climate import PRESET_COMFORT
from homeassistant.components.climate import PRESET_ECO
from homeassistant.components.climate import PRESET_NONE
from homeassistant.const import UnitOfTemperature
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import X4FP
from pyecodevices_rt2.exceptions import EcoDevicesRT2RequestError

from ..const import PRESET_COMFORT_1
from ..const import PRESET_COMFORT_2
from ..device_ecodevicesrt2 import EcoDevicesRT2Device

_LOGGER = logging.getLogger(__name__)

MODE_LIST = [HVACMode.HEAT, HVACMode.OFF]
PRESET_LIST = [
    PRESET_NONE,
    PRESET_COMFORT,
    PRESET_ECO,
    PRESET_AWAY,
    PRESET_COMFORT_1,
    PRESET_COMFORT_2,
]


class Climate_X4FP(EcoDevicesRT2Device, ClimateEntity):
    RT2_TO_HA_STATE = {
        0: PRESET_COMFORT,
        1: PRESET_ECO,
        2: PRESET_AWAY,
        3: PRESET_NONE,
        4: PRESET_COMFORT_1,
        5: PRESET_COMFORT_2,
    }
    HA_TO_RT2_STATE = {
        PRESET_COMFORT: 0,
        PRESET_ECO: 1,
        PRESET_AWAY: 2,
        PRESET_NONE: 3,
        PRESET_COMFORT_1: 4,
        PRESET_COMFORT_2: 5,
    }

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        module_id: int,
        zone_id: int,
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        self._module_id = module_id
        self._zone_id = zone_id
        self._available = True
        self.control = X4FP(ecort2, self._module_id, self._zone_id)
        self._device_class = "climate__x4fp"
        self._fp_state = 0
        self._enable_turn_on_off_backwards_compatibility = False
        self._attr_supported_features = (
            ClimateEntityFeature.TARGET_TEMPERATURE
            | ClimateEntityFeature.TURN_OFF
            | ClimateEntityFeature.TURN_ON
        )
        self._attr_translation_key = "climate__x4fp"

    def get_mode(self, cached_ms: int = None):
        return self.control.get_mode(cached_ms=cached_ms)

    def set_mode(self, mode: int):
        self.control.mode = mode

    @property
    def temperature_unit(self):
        """Return the unit of measurement used by the platform."""
        return UnitOfTemperature.CELSIUS

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return ClimateEntityFeature.PRESET_MODE

    @property
    def available(self):
        """Return true if switch is available."""
        return self._available

    @property
    def hvac_modes(self):
        """Return the list of available hvac operation modes.

        Need to be a subset of HVAC_MODES.
        """
        return MODE_LIST

    @property
    def hvac_mode(self):
        """Return hvac operation ie. heat, cool mode.

        Need to be one of HVAC_MODE_*.
        """
        if self.preset_mode == PRESET_NONE:
            return HVACMode.OFF
        return HVACMode.HEAT

    @property
    def preset_modes(self):
        """Return a list of available preset modes.

        Requires SUPPORT_PRESET_MODE.
        """
        return PRESET_LIST

    @property
    def preset_mode(self):
        """Return the current preset mode, e.g., home, away, temp.

        Requires SUPPORT_PRESET_MODE.
        """
        try:
            self._fp_state = self.get_mode()
            self._available = True
        except Exception as e:
            _LOGGER.error(
                "Device data no retrieve %s: %s (%s)",
                self.name,
                e,
                inspect.iscoroutinefunction(object),
            )
            self._available = False
        return self.RT2_TO_HA_STATE.get(self._fp_state)

    async def async_set_hvac_mode(self, hvac_mode):
        """Set new hvac mode."""
        if hvac_mode == HVACMode.OFF:
            await self.async_turn_off()
        elif hvac_mode == HVACMode.HEAT:
            await self.async_turn_on()
        await self.coordinator.async_request_refresh()

    async def async_turn_on(self):
        """Turn device on."""
        await self.async_set_preset_mode(PRESET_COMFORT)

    async def async_turn_off(self):
        """Turn device off."""
        await self.async_set_preset_mode(PRESET_NONE)

    async def async_set_preset_mode(self, preset_mode):
        """Set new preset mode."""
        try:
            await self.hass.async_add_executor_job(
                self.set_mode, self.HA_TO_RT2_STATE.get(preset_mode)
            )
            self._available = True
        except EcoDevicesRT2RequestError as e:
            _LOGGER.warning(
                "Error while changing mode (%s) device %s. Error: %s",
                preset_mode,
                self._name,
                e,
            )
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False

        await self.coordinator.async_request_refresh()
