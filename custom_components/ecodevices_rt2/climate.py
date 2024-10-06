"""Support for the GCE Ecodevices RT2 controller."""  # fmt: skip
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .climates import Climate_X4FP
from .const import CONF_DEVICES
from .const import CONF_MODULE_ID
from .const import CONF_TYPE
from .const import CONF_ZONE_ID
from .const import CONTROLLER
from .const import COORDINATOR
from .const import DOMAIN
from .const import TYPE_X4FP

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Set up the GCE Ecodevices RT2 climates."""
    controller = hass.data[DOMAIN][entry.entry_id][CONTROLLER]
    coordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]
    devices = hass.data[DOMAIN][entry.entry_id][CONF_DEVICES]["climate"]

    entities = []

    for device in devices:
        if device.get(CONF_TYPE) == TYPE_X4FP:
            entities.append(
                Climate_X4FP(
                    device,
                    controller,
                    coordinator,
                    device.get(CONF_MODULE_ID),
                    device.get(CONF_ZONE_ID),
                )
            )

    async_add_entities(entities, True)
