from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import Toroid

from . import Sensor_EcoDevicesRT2
from ..const import DEFAULT_ICON_CURRENCY
from ..const import DEFAULT_ICON_ENERGY


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

        # Allow overriding of currency unit and icon if specified in the conf
        if device_class is None:
            if not self._unit_of_measurement:
                self._unit_of_measurement = "€"
            if not self._icon:
                self._icon = DEFAULT_ICON_CURRENCY
        elif device_class == DEVICE_CLASS_ENERGY:
            self._unit_of_measurement = "kWh"
            self._icon = DEFAULT_ICON_ENERGY


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

    def _async_get_property(self):
        return self.control.consumption_price


class Sensor_Toroid_ProductionPrice(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "ProductionPrice")

    def _async_get_property(self):
        return self.control.production_price


class Sensor_Toroid_Index(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ENERGY, "Index")

    def _async_get_property(self):
        return self.control.value


class Sensor_Toroid_Price(Sensor_Toroid):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, None, "Price")

    def _async_get_property(self):
        return self.control.price
