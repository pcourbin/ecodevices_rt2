from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import SupplierIndex

from . import Sensor_EcoDevicesRT2


class Sensor_SupplierIndex(Sensor_EcoDevicesRT2):
    """Representation of an SupplierIndex sensor."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            device_class,
            suffix_name,
        )
        self.control = SupplierIndex(ecort2, self._id)


class Sensor_SupplierIndex_Index(Sensor_SupplierIndex):
    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            SensorDeviceClass.ENERGY,
            "Index",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_value(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_SupplierIndex_Price(Sensor_SupplierIndex):
    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            SensorDeviceClass.MONETARY,
            "Price",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_price(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
