from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import Toroid

from . import Sensor_EcoDevicesRT2


class Sensor_Toroid(Sensor_EcoDevicesRT2, Entity):
    """Representation of an Toroid_Sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self.control = Toroid(ecort2, self._id)
        self._device_class = device_class


class Sensor_Toroid_ConsumptionIndex(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "ConsumptionIndex")

    def _async_get_property(self):
        return self.control.consumption


class Sensor_Toroid_ProductionIndex(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "ProductionIndex")

    def _async_get_property(self):
        return self.control.production


class Sensor_Toroid_ConsumptionPrice(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "ConsumptionPrice")
        self._icon = "mdi:cash-multiple"

    def _async_get_property(self):
        return self.control.consumption_price


class Sensor_Toroid_ProductionPrice(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "ProductionPrice")
        self._icon = "mdi:cash-multiple"

    def _async_get_property(self):
        return self.control.production_price
