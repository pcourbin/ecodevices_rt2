from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import SupplierIndex

from . import Sensor_EcoDevicesRT2


class Sensor_SupplierIndex(Sensor_EcoDevicesRT2, Entity):
    """Representation of an SupplierIndex sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self.control = SupplierIndex(ecort2, self._id)
        self._device_class = device_class


class Sensor_SupplierIndex_Index(Sensor_SupplierIndex):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "Index")

    def _async_get_property(self):
        return self.control.value


class Sensor_SupplierIndex_Price(Sensor_SupplierIndex):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "Price")
        self._icon = "mdi:cash-multiple"

    def _async_get_property(self):
        return self.control.price
