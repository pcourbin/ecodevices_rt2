from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import Counter
from pyecodevices_rt2 import EcoDevicesRT2

from . import Sensor_EcoDevicesRT2


class Sensor_Counter(Sensor_EcoDevicesRT2):
    """Representation of an Counter_Sensor sensor."""

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
            hass, device_config, ecort2, coordinator, device_class, suffix_name
        )
        self.control = Counter(ecort2, self._id)


class Sensor_Counter_Index(Sensor_Counter):
    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        device_class = SensorDeviceClass.ENERGY
        if device_config.get("device_class"):
            device_class = device_config.get("device_class")
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            device_class,
            "Index",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_value(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_Counter_Price(Sensor_Counter):
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
