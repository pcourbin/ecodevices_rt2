import logging

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import XTHL

from . import Sensor_EcoDevicesRT2


_LOGGER = logging.getLogger(__name__)


class Sensor_XTHL(Sensor_EcoDevicesRT2):
    """Representation of a X-THL sensor."""

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
        self.control = XTHL(ecort2, self._id)


class Sensor_XTHL_Temp(Sensor_XTHL):
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
            SensorDeviceClass.TEMPERATURE,
            "Temperature",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_temperature(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_XTHL_Hum(Sensor_XTHL):
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
            SensorDeviceClass.HUMIDITY,
            "Humidity",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_humidity(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value


class Sensor_XTHL_Lum(Sensor_XTHL):
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
            SensorDeviceClass.ILLUMINANCE,
            "Luminance",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_luminosity(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
