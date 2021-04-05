"""Support for the GCE Eco-Devices RT2."""
""" Based on work of @Mati24 -- https://github.com/Aohzan/ecodevices"""
import voluptuous as vol
import logging

from .ecodevicesapi import ECODEVICE as ecodevice

from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_NAME,
    CONF_API_KEY,
    CONF_ICON,
    CONF_UNIT_OF_MEASUREMENT,
    CONF_DEVICE_CLASS,
)

_LOGGER = logging.getLogger(__name__)

CONF_RT2_IN = "rt2_command"
CONF_RT2_IN_DETAIL = "rt2_command_value"
CONF_RT2_NAME = "rt2_command_entry"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=80): cv.port,
        vol.Optional(CONF_API_KEY, default=""): cv.string,
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_RT2_IN, default="Index"): cv.string,
        vol.Optional(CONF_RT2_IN_DETAIL, default="All"): cv.string,
        vol.Optional(CONF_RT2_NAME): cv.string,
        vol.Optional(CONF_ICON, default="mdi:flash"): cv.string,
        vol.Optional(CONF_UNIT_OF_MEASUREMENT, default="W"): cv.string,
        vol.Optional(CONF_DEVICE_CLASS, default="power"): cv.string,
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
                EcoDevice_Sensor(
                    controller,
                    config.get(CONF_RT2_IN),
                    config.get(CONF_RT2_IN_DETAIL),
                    config.get(CONF_RT2_NAME),
                    config.get(CONF_NAME),
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
        add_entities(entities, True)


class EcoDevice_Sensor(Entity):
    """Representation of a Sensor."""

    def __init__(self, controller, request_in, resquest_in_detail, request_name, name, unit, icon, device_class):
        """Initialize the sensor."""
        self._controller = controller
        self._request_in = request_in
        self._request_in_detail = resquest_in_detail
        self._request_name = request_name
        self._name = name
        self._unit = unit
        self._icon = icon
        self._device_class = device_class

        self._state = None
        self._uid = f"{self._controller.host}_{str(self._request_name)}"

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
            self._state = await self.hass.async_add_executor_job(self._controller.get, self._request_in, self._request_in_detail, self._request_name)
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False
