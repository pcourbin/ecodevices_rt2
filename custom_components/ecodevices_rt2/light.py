"""Support for the GCE Ecodevices RT2 controller."""
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import CONF_API_GET
from .const import CONF_API_GET_ENTRY
from .const import CONF_API_GET_VALUE
from .const import CONF_API_OFF_GET
from .const import CONF_API_OFF_GET_VALUE
from .const import CONF_API_ON_GET
from .const import CONF_API_ON_GET_VALUE
from .const import CONF_DEVICES
from .const import CONF_TYPE
from .const import CONTROLLER
from .const import DOMAIN
from .const import TYPE_API
from .const import TYPE_ENOCEAN
from .const import TYPE_RELAY
from .const import TYPE_VIRTUALOUTPUT
from .lights import Light_API
from .lights import Light_EnOcean
from .lights import Light_Relay
from .lights import Light_VirtualOutput

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Set up the GCE Ecodevices RT2 lights."""
    controller = hass.data[DOMAIN][entry.entry_id][CONTROLLER]
    devices = hass.data[DOMAIN][entry.entry_id][CONF_DEVICES]["light"]

    entities = []

    for device in devices:
        if device.get(CONF_TYPE) == TYPE_API:
            entities.append(
                Light_API(
                    device,
                    controller,
                    device.get(CONF_API_GET),
                    device.get(CONF_API_GET_VALUE),
                    device.get(CONF_API_GET_ENTRY),
                    device.get(CONF_API_ON_GET),
                    device.get(CONF_API_ON_GET_VALUE),
                    device.get(CONF_API_OFF_GET),
                    device.get(CONF_API_OFF_GET_VALUE),
                )
            )
        elif device.get(CONF_TYPE) == TYPE_ENOCEAN:
            entities.append(Light_EnOcean(device, controller))
        elif device.get(CONF_TYPE) == TYPE_RELAY:
            entities.append(Light_Relay(device, controller))
        elif device.get(CONF_TYPE) == TYPE_VIRTUALOUTPUT:
            entities.append(Light_VirtualOutput(device, controller))

    async_add_entities(entities, True)
