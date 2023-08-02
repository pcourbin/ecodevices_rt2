from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.const import UnitOfEnergy
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import Post

from . import Sensor_EcoDevicesRT2
from ..const import CONF_SUBPOST_ID
from ..const import CONF_UNIT_INDEX


class Sensor_Post(Sensor_EcoDevicesRT2):
    """Representation of an Post_Sensor."""

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
        if CONF_SUBPOST_ID in device_config:
            self.control = Post(ecort2, self._id, device_config[CONF_SUBPOST_ID])
        else:
            self.control = Post(ecort2, self._id)

        if device_class == SensorDeviceClass.ENERGY and not device_config.get(
            CONF_UNIT_INDEX
        ):
            self._unit_of_measurement = UnitOfEnergy.KILO_WATT_HOUR


class Sensor_Post_Index(Sensor_Post):
    def __init__(
        self,
        hass,
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
        value = self.control.get_index(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_Post_Price(Sensor_Post):
    def __init__(
        self,
        hass,
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


class Sensor_Post_IndexDay(Sensor_Post):
    def __init__(
        self,
        hass,
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
            "IndexDay",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_index_day(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_Post_PriceDay(Sensor_Post):
    def __init__(
        self,
        hass,
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
            "PriceDay",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_price_day(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_Post_Instant(Sensor_Post):
    def __init__(
        self,
        hass,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            SensorDeviceClass.POWER,
            "Instant",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_instant(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
