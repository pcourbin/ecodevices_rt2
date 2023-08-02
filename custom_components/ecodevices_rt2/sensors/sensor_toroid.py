from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import Toroid

from . import Sensor_EcoDevicesRT2


class Sensor_Toroid(Sensor_EcoDevicesRT2):
    """Representation of an Toroid_Sensor."""

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
        self.control = Toroid(ecort2, self._id)


class Sensor_Toroid_Index(Sensor_Toroid):
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


class Sensor_Toroid_Price(Sensor_Toroid):
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
