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
from .const import CONF_MODULE_ID
from .const import CONF_TYPE
from .const import CONF_ZONE_ID
from .const import CONTROLLER
from .const import COORDINATOR
from .const import DOMAIN
from .const import TYPE_API
from .const import TYPE_ENOCEAN
from .const import TYPE_RELAY
from .const import TYPE_VIRTUALOUTPUT
from .const import TYPE_X4FP
from .switches import Switch_API
from .switches import Switch_EnOcean
from .switches import Switch_Relay
from .switches import Switch_VirtualOutput
from .switches import Switch_X4FP

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Set up the GCE Ecodevices RT2 switches."""
    controller = hass.data[DOMAIN][entry.entry_id][CONTROLLER]
    coordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]
    devices = hass.data[DOMAIN][entry.entry_id][CONF_DEVICES]["switch"]

    entities = []

    for device in devices:

        if device.get(CONF_TYPE) == TYPE_API:
            entities.append(
                Switch_API(
                    device,
                    controller,
                    coordinator,
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
            entities.append(Switch_EnOcean(device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_RELAY:
            entities.append(Switch_Relay(device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_VIRTUALOUTPUT:
            entities.append(Switch_VirtualOutput(device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_X4FP:
            entities.append(
                Switch_X4FP(
                    device,
                    controller,
                    coordinator,
                    device.get(CONF_MODULE_ID),
                    device.get(CONF_ZONE_ID),
                )
            )

    async_add_entities(entities, True)
