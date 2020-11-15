"""Support for the GCE Eco-Devices RT2."""
import voluptuous as vol

import asyncio

import logging

from .ecodevicesapi import ECODEVICE as ecodevice

from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity
from homeassistant.helpers.entity import Entity
import homeassistant.helpers.config_validation as cv

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
)

_LOGGER = logging.getLogger(__name__)

RT2_SWITCH_RESPONSE_ENTRY = "status"
RT2_SWITCH_RESPONSE_SUCCESS_VALUE = "Success"

CONF_RT2_COMMAND = "rt2_command"
CONF_RT2_COMMAND_VALUE = "rt2_command_value"
CONF_RT2_COMMAND_ENTRY = "rt2_command_entry"
CONF_RT2_ON_COMMAND = "rt2_on_command"
CONF_RT2_ON_COMMAND_VALUE = "rt2_on_command_value"
CONF_RT2_OFF_COMMAND = "rt2_off_command"
CONF_RT2_OFF_COMMAND_VALUE = "rt2_off_command_value"

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=80): cv.port,
        vol.Optional(CONF_API_KEY, default=""): cv.string,
        vol.Optional(CONF_NAME): cv.string,
        vol.Optional(CONF_RT2_COMMAND, default="Get"): cv.string,
        vol.Optional(CONF_RT2_COMMAND_VALUE, default="XENO"): cv.string,
        vol.Optional(CONF_RT2_COMMAND_ENTRY, default="ENO ACTIONNEUR1"): cv.string,
        vol.Optional(CONF_ICON, default="mdi:toggle-switch"): cv.string,
        vol.Optional(CONF_DEVICE_CLASS, default="switch"): cv.string,
        vol.Optional(CONF_RT2_ON_COMMAND, default="SetEnoPC"): cv.string,
        vol.Optional(CONF_RT2_ON_COMMAND_VALUE, default="1"): cv.string,
        vol.Optional(CONF_RT2_OFF_COMMAND, default="ClearEnoPC"): cv.string,
        vol.Optional(CONF_RT2_OFF_COMMAND_VALUE, default="1"): cv.string,
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
                EcoDevice_Switch(
                    controller,
                    config.get(CONF_RT2_COMMAND),
                    config.get(CONF_RT2_COMMAND_VALUE),
                    config.get(CONF_RT2_COMMAND_ENTRY),
                    config.get(CONF_NAME),
                    config.get(CONF_ICON),
                    config.get(CONF_DEVICE_CLASS),
                    config.get(CONF_RT2_ON_COMMAND),
                    config.get(CONF_RT2_ON_COMMAND_VALUE),
                    config.get(CONF_RT2_OFF_COMMAND),
                    config.get(CONF_RT2_OFF_COMMAND_VALUE),
                )
            )
    else:
        _LOGGER.error(
            "Can't connect to the plateform %s, please check host and port.",
            config.get(CONF_HOST),
        )
    if entities:
        add_entities(entities, True)


class EcoDevice_Switch(SwitchEntity):
    """Representation of a Switch."""

    def __init__(self, controller, command, command_value, command_entry, name, icon, device_class, on_command, on_command_value, off_command, off_command_value):
        """Initialize the switch."""
        self._controller = controller
        self._command = command
        self._command_value = command_value
        self._command_entry = command_entry
        self._name = name
        self._icon = icon
        self._device_class = device_class

        self._available = True
        self._is_on = False

        self._on_command = on_command
        self._on_command_value = on_command_value
        self._off_command = off_command
        self._off_command_value = off_command_value

        self._uid = f"{self._controller.host}_{str(self._command_entry)}_switch"

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
    def is_on(self):
        """Return true if switch is on. Standby is on."""
        return self._is_on

    @property
    def available(self):
        """Return true if switch is available."""
        return self._available

    async def async_turn_on(self, **kwargs):
        """Turn the switch on."""
        if self._controller.get(self._on_command, self._on_command_value, RT2_SWITCH_RESPONSE_ENTRY) == RT2_SWITCH_RESPONSE_SUCCESS_VALUE:
            self._is_on = True
        else:
            _LOGGER.warning("Error while turning on device %s", self._name)
            #self._available = False

        self.schedule_update_ha_state()

    async def async_turn_off(self, **kwargs):
        if self._controller.get(self._off_command, self._off_command_value, RT2_SWITCH_RESPONSE_ENTRY) == RT2_SWITCH_RESPONSE_SUCCESS_VALUE:
            self._is_on = False
        else:
            _LOGGER.warning("Error while turning off device %s", self._name)
            #self._available = False

        self.schedule_update_ha_state()

    async def async_update(self):        
        self._is_on = (self._controller.get(self._command, self._command_value, self._command_entry) == 1)
