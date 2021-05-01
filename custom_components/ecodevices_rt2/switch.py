"""Support for the GCE controller."""
import asyncio
import voluptuous as vol
import logging

from pyecodevices_rt2 import EcoDevicesRT2
from .const import (
    DOMAIN,
    CONFIG,
    CONTROLLER,
    RT2_RESPONSE_ENTRY,
    RT2_RESPONSE_SUCCESS_VALUE,
    CONF_RT2_COMMAND,
    CONF_RT2_COMMAND_VALUE,
    CONF_RT2_COMMAND_ENTRY,
    CONF_RT2_ON_COMMAND,
    CONF_RT2_ON_COMMAND_VALUE,
    CONF_RT2_OFF_COMMAND,
    CONF_RT2_OFF_COMMAND_VALUE,
)

from homeassistant.config_entries import SOURCE_IMPORT
import homeassistant.helpers.config_validation as cv
from homeassistant.components.switch import PLATFORM_SCHEMA, SwitchEntity

from homeassistant.const import (
    CONF_HOST,
    CONF_PORT,
    CONF_FRIENDLY_NAME,
    CONF_API_KEY,
    CONF_ICON,
    CONF_DEVICE_CLASS,
    STATE_OFF,
    STATE_ON,
    STATE_STANDBY,
    STATE_UNKNOWN,
)

_LOGGER = logging.getLogger(__name__)

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend(
    {
        vol.Required(CONF_HOST): cv.string,
        vol.Optional(CONF_PORT, default=80): cv.port,
        vol.Optional(CONF_API_KEY, default=""): cv.string,
        vol.Required(CONF_FRIENDLY_NAME): cv.string,
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
                EcoDevice_Switch(
                    controller,
                    config.get(CONF_RT2_COMMAND),
                    config.get(CONF_RT2_COMMAND_VALUE),
                    config.get(CONF_RT2_COMMAND_ENTRY),
                    config.get(CONF_FRIENDLY_NAME),
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
        async_add_entities(entities, True)

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
        self._is_on_command = self._is_on
        self._updated = True

        self._on_command = on_command
        self._on_command_value = on_command_value
        self._off_command = off_command
        self._off_command_value = off_command_value

        self._uid = f"{self._controller.host}_{str(self._command)}_{str(self._command_value)}_{str(self._command_entry)}_switch"

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
        return f"ecodevices-rt2_{self._controller.host}_{str(self._command)}_{str(self._command_value)}_{str(self._command_entry)}"

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

    async def async_update(self):
        try:
            temp = await self.hass.async_add_executor_job(self._controller.get, self._command, self._command_value, self._command_entry)
            self._is_on = (temp == 1)
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False     
        
        if (self._is_on_command != self._is_on):
            if (self._updated == False):
                if (self._is_on_command == True):
                    try:
                        temp = await self.hass.async_add_executor_job(self._controller.get, self._on_command, self._on_command_value, RT2_RESPONSE_ENTRY)
                        if temp == RT2_RESPONSE_SUCCESS_VALUE:
                            self._available = True
                            self._updated = True
                        else:
                            _LOGGER.warning("Error while turning on device %s", self._name)
                    except Exception as e:
                        _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
                        self._available = False   
                else:
                    try:
                        temp = await self.hass.async_add_executor_job(self._controller.get, self._off_command, self._off_command_value, RT2_RESPONSE_ENTRY)
                        if temp == RT2_RESPONSE_SUCCESS_VALUE:
                            self._available = True
                            self._updated = True
                        else:
                            _LOGGER.warning("Error while turning off device %s", self._name)
                    except Exception as e:
                        _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
                        self._available = False
            else:
                self._is_on_command = self._is_on
        
