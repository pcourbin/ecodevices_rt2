"""Support for the GCE Ecodevices RT2 controller."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .binarysensors import BinarySensor_DigitalInput
from .const import CONF_DEVICES
from .const import CONF_TYPE
from .const import CONTROLLER
from .const import DOMAIN
from .const import TYPE_DIGITALLINPUT

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Set up the GCE Ecodevices RT2 binary_sensors."""
    controller = hass.data[DOMAIN][entry.entry_id][CONTROLLER]
    devices = hass.data[DOMAIN][entry.entry_id][CONF_DEVICES]["binary_sensor"]

    entities = []

    for device in devices:
        if device.get(CONF_TYPE) == TYPE_DIGITALLINPUT:
            entities.append(BinarySensor_DigitalInput(device, controller))

    async_add_entities(entities, True)
