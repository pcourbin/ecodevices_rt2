"""Support for the GCE Eco-Devices RT2."""
import asyncio
import voluptuous as vol
import logging
from datetime import timedelta

from .ecodevicesapi import ECODEVICE as ecodevice

from homeassistant.components.sensor import PLATFORM_SCHEMA
import homeassistant.helpers.config_validation as cv
from homeassistant.components.climate import ClimateEntity
from homeassistant.components.climate.const import (
    HVAC_MODE_HEAT,
    HVAC_MODE_OFF,
    PRESET_AWAY,
    PRESET_COMFORT,
    PRESET_ECO,
    PRESET_NONE,
    SUPPORT_PRESET_MODE,
)
from homeassistant.util import Throttle
from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_NAME,
    CONF_API_KEY,
    CONF_ICON,
    CONF_DEVICE_CLASS,
    STATE_OFF,
    STATE_ON,
    STATE_STANDBY,
    STATE_UNKNOWN,
    TEMP_CELSIUS
)

MODE_LIST = [HVAC_MODE_HEAT, HVAC_MODE_OFF]
PRESET_LIST = [PRESET_NONE, PRESET_COMFORT, PRESET_ECO, PRESET_AWAY]

_LOGGER = logging.getLogger(__name__)

RT2_RESPONSE_ENTRY = "status"
RT2_RESPONSE_SUCCESS_VALUE = "Success"
RT2_FP_GET_COMMAND = "Get"
RT2_FP_GET_COMMAND_VALUE = "FP"
RT2_FP_GET_COMMAND_ENTRY = "FP%s Zone %s"
RT2_FP_SET_COMMAND = "SetFP0%s"

CONF_RT2_FP_EXT = "rt2_fp_ext"
CONF_RT2_FP_ZONE = "rt2_fp_zone"
SCAN_INTERVAL = timedelta(minutes=1)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=80): cv.port,
        vol.Optional(CONF_API_KEY, default=""): cv.string,
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_RT2_FP_EXT, default="1"): cv.string,
        vol.Optional(CONF_RT2_FP_ZONE, default="1"): cv.string,
    }
)


def setup_platform(hass, config, add_entities, discovery_info=None):
    """Set up the GCE Eco-Devices platform."""
    controller = ecodevice(config.get(CONF_HOST), config.get(CONF_PORT), config.get(CONF_API_KEY))
    entities = []

    if controller.ping():
        _LOGGER.info(
            "Successfully connected to the Eco-Device RT2 gateway: %s.",
            config.get(CONF_HOST, CONF_PORT),
        )
        if config.get(CONF_NAME):
            _LOGGER.info("Add the device with name: %s.", config.get(CONF_NAME))
            entities.append(
                EcoDevice_Thermostat(
                    controller,
                    config.get(CONF_NAME),
                    config.get(CONF_ICON),
                    config.get(CONF_DEVICE_CLASS),
                    config.get(CONF_RT2_FP_EXT),
                    config.get(CONF_RT2_FP_ZONE),
                )
            )
    else:
        _LOGGER.error(
            "Can't connect to the plateform %s, please check host and port.",
            config.get(CONF_HOST),
        )
    if entities:
        add_entities(entities, True)


class EcoDevice_Thermostat(ClimateEntity):
    """Representation of a Switch."""

    RT2_TO_HA_STATE = {
    "Confort": PRESET_COMFORT,
    "Eco": PRESET_ECO,
    "Hors Gel": PRESET_AWAY,
    "Arret": PRESET_NONE,
    }
    HA_TO_RT2_STATE = {
        PRESET_COMFORT: 0,
        PRESET_ECO: 1,
        PRESET_AWAY: 2,
        PRESET_NONE: 3,
    }

    def __init__(self, controller, name, icon, device_class, fp_ext, fp_zone):
        """Initialize the switch."""
        self._controller = controller
        self._name = name
        self._icon = icon
        self._device_class = device_class

        self._fp_ext = fp_ext
        self._fp_zone = fp_zone
        self._fp_zone_get = fp_zone
        if (self._fp_ext == 2):
            self._fp_zone_get = self._fp_zone_get + 4
        self._fp_state = None
        self._available = True

        self._set_command = RT2_FP_SET_COMMAND % (str(self._fp_zone_get))
        self._get_command_entry = RT2_FP_GET_COMMAND_ENTRY % (str(self._fp_ext), str(self._fp_zone))

        self._uid = f"{self._controller.host}_FP{str(self._fp_ext)}_Zone{str(self._fp_zone)}_thermostat"

    @property
    def device_info(self):
        return {
            "identifiers": {("ecodevices", self._uid)},
            "name": self._name,
            "manufacturer": "GCE",
            "model": "ECO-DEVICES-RT2",
            "via_device": ("ecodevices", self._controller.host),
        }

    @property
    def unique_id(self):
        return self._uid

    @property
    def device_class(self):
        return self._device_class

    @property
    def name(self):
        return self._name

    @property
    def icon(self):
        return self._icon

    @property
    def temperature_unit(self):
        """Return the unit of measurement used by the platform."""
        return TEMP_CELSIUS

    @property
    def supported_features(self):
        """Return the list of supported features."""
        return SUPPORT_PRESET_MODE

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
            return HVAC_MODE_OFF
        return HVAC_MODE_HEAT

    @property
    def preset_modes(self):
        """Return a list of available preset modes.

        Requires SUPPORT_PRESET_MODE.
        """
        return PRESET_LIST

    async def async_set_hvac_mode(self, hvac_mode):
        """Set new hvac mode."""
        if hvac_mode == HVAC_MODE_OFF:
            await self.async_turn_off()
        elif hvac_mode == HVAC_MODE_HEAT:
            await self.async_turn_on()

    async def async_turn_on(self):
        """Turn device on."""
        await self.async_set_preset_mode(PRESET_COMFORT)

    async def async_turn_off(self):
        """Turn device off."""
        await self.async_set_preset_mode(PRESET_NONE)

    async def async_update_heater(self, force_update=False):
        """Get the latest state from the thermostat."""
        if force_update is True:
            # Updated temperature to HA state to avoid flapping (API confirmation is slow)
            await asyncio.sleep(1)
        try:
            self._fp_state = await self.hass.async_add_executor_job(self._controller.get, RT2_FP_GET_COMMAND, RT2_FP_GET_COMMAND_VALUE, self._get_command_entry)
            if self._fp_state:
                self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False

    @Throttle(SCAN_INTERVAL)
    async def async_update(self):
        """Update device."""
        await self.async_update_heater()

    @property
    def preset_mode(self):
        """Return the current preset mode, e.g., home, away, temp.

        Requires SUPPORT_PRESET_MODE.
        """
        return self.RT2_TO_HA_STATE.get(self._fp_state)

    async def async_set_preset_mode(self, preset_mode):
        """Set new preset mode."""
        try:
            temp = await self.hass.async_add_executor_job(self._controller.get, self._set_command, self.HA_TO_RT2_STATE.get(preset_mode), RT2_RESPONSE_ENTRY)
            if temp == RT2_RESPONSE_SUCCESS_VALUE:
                self._available = True
            else:
                _LOGGER.warning("Error while changing mode (%s) device %s", preset_mode, self._name)
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False

        await self.async_update_heater(True)

        
