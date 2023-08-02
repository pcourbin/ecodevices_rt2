import logging

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import XTHL

from . import Sensor_EcoDevicesRT2


_LOGGER = logging.getLogger(__name__)


class Sensor_XTHL(Sensor_EcoDevicesRT2):
    """Representation of a X-THL sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        self.control = XTHL(ecort2, self._id)
        self._device_class = device_class
        self._state_class = STATE_CLASS_MEASUREMENT
        # Allow overriding of temperature unit if specified in the conf
        if (
            device_class == SensorDeviceClass.TEMPERATURE
            and not self._unit_of_measurement
        ):
            self._unit_of_measurement = "°C"
        elif device_class == SensorDeviceClass.HUMIDITY:
            self._unit_of_measurement = "%"
        elif device_class == SensorDeviceClass.ILLUMINANCE:
            self._unit_of_measurement = "lx"


class Sensor_XTHL_Temp(Sensor_XTHL):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
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
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
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
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
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
