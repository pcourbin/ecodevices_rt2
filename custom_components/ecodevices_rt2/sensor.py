"""Support for the GCE Ecodevices RT2.
Based on work of @Mati24 -- https://github.com/Aohzan/ecodevices"""  # fmt: skip
import logging

from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import CONF_API_GET
from .const import CONF_API_GET_ENTRY
from .const import CONF_API_GET_VALUE
from .const import CONF_DEVICES
from .const import CONF_TYPE
from .const import CONTROLLER
from .const import COORDINATOR
from .const import DOMAIN
from .const import TYPE_API
from .const import TYPE_COUNTER
from .const import TYPE_ENOCEAN
from .const import TYPE_POST
from .const import TYPE_SUPPLIERINDEX
from .const import TYPE_TOROID
from .const import TYPE_XTHL
from .sensors import Sensor_API
from .sensors import Sensor_Counter_Index
from .sensors import Sensor_Counter_Price
from .sensors import Sensor_EnOcean
from .sensors import Sensor_Post_Index
from .sensors import Sensor_Post_IndexDay
from .sensors import Sensor_Post_Instant
from .sensors import Sensor_Post_Price
from .sensors import Sensor_Post_PriceDay
from .sensors import Sensor_SupplierIndex_Index
from .sensors import Sensor_SupplierIndex_Price
from .sensors import Sensor_Toroid_Index
from .sensors import Sensor_Toroid_Price
from .sensors import Sensor_XTHL_Hum
from .sensors import Sensor_XTHL_Lum
from .sensors import Sensor_XTHL_Temp

_LOGGER = logging.getLogger(__name__)


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities,
) -> None:
    """Set up the GCE Ecodevices RT2 sensors."""
    controller = hass.data[DOMAIN][entry.entry_id][CONTROLLER]
    coordinator = hass.data[DOMAIN][entry.entry_id][COORDINATOR]
    devices = hass.data[DOMAIN][entry.entry_id][CONF_DEVICES]["sensor"]

    entities = []

    for device in devices:
        if device.get(CONF_TYPE) == TYPE_API:
            entities.append(
                Sensor_API(
                    hass,
                    device,
                    controller,
                    coordinator,
                    device.get(CONF_API_GET),
                    device.get(CONF_API_GET_VALUE),
                    device.get(CONF_API_GET_ENTRY),
                )
            )
        elif device.get(CONF_TYPE) == TYPE_COUNTER:
            entities.append(Sensor_Counter_Index(hass, device, controller, coordinator))
            entities.append(Sensor_Counter_Price(hass, device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_ENOCEAN:
            entities.append(Sensor_EnOcean(hass, device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_POST:
            entities.append(Sensor_Post_Index(hass, device, controller, coordinator))
            entities.append(Sensor_Post_Price(hass, device, controller, coordinator))
            entities.append(Sensor_Post_IndexDay(hass, device, controller, coordinator))
            entities.append(Sensor_Post_PriceDay(hass, device, controller, coordinator))
            entities.append(Sensor_Post_Instant(hass, device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_SUPPLIERINDEX:
            entities.append(
                Sensor_SupplierIndex_Index(hass, device, controller, coordinator)
            )
            entities.append(
                Sensor_SupplierIndex_Price(hass, device, controller, coordinator)
            )
        elif device.get(CONF_TYPE) == TYPE_TOROID:
            entities.append(Sensor_Toroid_Index(hass, device, controller, coordinator))
            entities.append(Sensor_Toroid_Price(hass, device, controller, coordinator))
        elif device.get(CONF_TYPE) == TYPE_XTHL:
            entities.append(Sensor_XTHL_Temp(hass, device, controller, coordinator))
            entities.append(Sensor_XTHL_Hum(hass, device, controller, coordinator))
            entities.append(Sensor_XTHL_Lum(hass, device, controller, coordinator))

    async_add_entities(entities, True)
