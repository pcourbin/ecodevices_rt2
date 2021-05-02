from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import Counter
from pyecodevices_rt2 import EcoDevicesRT2

from . import Sensor_EcoDevicesRT2


class Sensor_Counter(Sensor_EcoDevicesRT2, Entity):
    """Representation of an Counter_Sensor sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self.control = Counter(ecort2, self._id)
        self._device_class = device_class


class Sensor_Counter_Index(Sensor_Counter):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "Index")

    def _async_get_property(self):
        return self.control.value


class Sensor_Counter_Price(Sensor_Counter):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "Price")
        self._icon = "mdi:cash-multiple"

    def _async_get_property(self):
        return self.control.price
