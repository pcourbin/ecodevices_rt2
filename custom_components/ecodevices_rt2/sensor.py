"""Support for the GCE Ecodevices RT2."""
""" Based on work of @Mati24 -- https://github.com/Aohzan/ecodevices"""
import voluptuous as vol
import logging

from pyecodevices_rt2 import EcoDevicesRT2
from .const import (
    DOMAIN,    
    CONFIG,
    CONTROLLER,
    CONF_RT2_COMMAND,
    CONF_RT2_COMMAND_VALUE,
    CONF_RT2_COMMAND_ENTRY,
)

from homeassistant.config_entries import SOURCE_IMPORT
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.entity import Entity
from homeassistant.components.sensor import PLATFORM_SCHEMA

from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_FRIENDLY_NAME,
    CONF_API_KEY,
    CONF_ICON,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_DEVICE_CLASS,
)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=80): cv.port,
        vol.Optional(CONF_API_KEY, default=""): cv.string,
        vol.Optional(CONF_FRIENDLY_NAME): cv.string,
        vol.Optional(CONF_RT2_COMMAND, default="Index"): cv.string,
        vol.Optional(CONF_RT2_COMMAND_VALUE, default="All"): cv.string,
        vol.Optional(CONF_RT2_COMMAND_ENTRY): cv.string,
        vol.Optional(CONF_ICON, default="mdi:flash"): cv.string,
        vol.Optional(CONF_UNIT_OF_MEASUREMENT, default="W"): cv.string,
        vol.Optional(CONF_DEVICE_CLASS, default="power"): cv.string,
    }
)


async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    """Set up the GCE Ecodevices RT2 platform."""
    controller = EcoDevicesRT2(config.get(CONF_HOST), config.get(CONF_PORT), config.get(CONF_API_KEY))
    entities = []

    try:
        if(await hass.async_add_executor_job(controller.ping) == True):
            available = True
        else:
            available = False
    except Exception:
        available = False

    if available == True:
        _LOGGER.info(
            "Successfully connected to the Ecodevice RT2 gateway: %s.",
            config.get(CONF_HOST, CONF_PORT),
        )
        if config.get(CONF_FRIENDLY_NAME):
            _LOGGER.info("Add the device with name: %s.", config.get(CONF_FRIENDLY_NAME))
            entities.append(
                EcoDevice_Sensor(
                    controller,
                    config.get(CONF_RT2_COMMAND),
                    config.get(CONF_RT2_COMMAND_VALUE),
                    config.get(CONF_RT2_COMMAND_ENTRY),
                    config.get(CONF_FRIENDLY_NAME),
                    config.get(CONF_UNIT_OF_MEASUREMENT),
                    config.get(CONF_ICON),
                    config.get(CONF_DEVICE_CLASS),
                )
            )
    else:
        _LOGGER.error(
            "Can't connect to the plateform %s, please check host and port.",
            config.get(CONF_HOST),
        )
    if entities:
        async_add_entities(entities, True)
    

class EcoDevice_Sensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, controller, command, command_value, command_entry, name, unit, icon, device_class):
        """Initialize the sensor."""
        self._controller = controller

        self._command = command
        self._command_value = command_value
        self._command_entry = command_entry
        self._name = name
        self._unit = unit
        self._icon = icon
        self._device_class = device_class

        self._state = None
        self._uid = f"{self._controller.host}_{str(self._command)}_{str(self._command_value)}_{str(self._command_entry)}"

    @property
    def device_info(self):
        return {
            "identifiers": {(DOMAIN, self._uid)},
            "name": self._name,
            "manufacturer": "GCE",
            "model": "Ecodevices RT2",
            "via_device": (DOMAIN, self._uid),
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
    def state(self):
        return self._state

    @property
    def unit_of_measurement(self):
        return self._unit

    @property
    def icon(self):
        return self._icon

    async def async_update(self):  #def update(self):
        try:
            self._state = await self.hass.async_add_executor_job(self._controller.get, self._command, self._command_value, self._command_entry)
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False
