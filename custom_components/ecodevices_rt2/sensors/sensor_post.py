from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.const import DEVICE_CLASS_POWER
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import Post

from . import Sensor_EcoDevicesRT2
from ..const import CONF_SUBPOST_ID


class Sensor_Post(Sensor_EcoDevicesRT2, Entity):
    """Representation of an Post_Sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, suffix_name)
        if CONF_SUBPOST_ID in device_config:
            self.control = Post(ecort2, self._id, device_config[CONF_SUBPOST_ID])
        else:
            self.control = Post(ecort2, self._id)
        self._device_class = device_class


class Sensor_Post_Index(Sensor_Post):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "Index")

    def _async_get_property(self):
        return self.control.index


class Sensor_Post_Price(Sensor_Post):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "Price")
        self._icon = "mdi:cash-multiple"

    def _async_get_property(self):
        return self.control.price


class Sensor_Post_IndexDay(Sensor_Post):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "IndexDay")

    def _async_get_property(self):
        return self.control.index_day


class Sensor_Post_PriceDay(Sensor_Post):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "PriceDay")
        self._icon = "mdi:cash-multiple"

    def _async_get_property(self):
        return self.control.price_day


class Sensor_Post_Instant(Sensor_Post):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_POWER, "Instant")

    def _async_get_property(self):
        return self.control.instant
