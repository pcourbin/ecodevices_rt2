import logging

from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import XTHL

from . import Sensor_EcoDevicesRT2
from ..const import CONF_DEVICE_CLASS
from ..const import CONF_STATE_CLASS


_LOGGER = logging.getLogger(__name__)


class Sensor_XTHL(Sensor_EcoDevicesRT2):
    """Representation of a X-THL sensor."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        suffix_name: str,
    ):
        super().__init__(hass, device_config, ecort2, coordinator, suffix_name)
        self.control = XTHL(ecort2, self._id)


class Sensor_XTHL_Temp(Sensor_XTHL):
    def __init__(
        self,
        hass: HomeAssistant,
        device_config_g: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        device_config = dict(device_config_g)
        device_config[CONF_DEVICE_CLASS] = SensorDeviceClass.TEMPERATURE
        device_config[CONF_STATE_CLASS] = SensorStateClass.MEASUREMENT
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
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
        device_config_g: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        device_config = dict(device_config_g)
        device_config[CONF_DEVICE_CLASS] = SensorDeviceClass.HUMIDITY
        device_config[CONF_STATE_CLASS] = SensorStateClass.MEASUREMENT
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
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
        device_config_g: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        device_config = dict(device_config_g)
        device_config[CONF_DEVICE_CLASS] = SensorDeviceClass.ILLUMINANCE
        device_config[CONF_STATE_CLASS] = SensorStateClass.MEASUREMENT
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            "Luminance",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_luminosity(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
