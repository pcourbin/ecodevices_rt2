import logging

from homeassistant.const import DEVICE_CLASS_HUMIDITY
from homeassistant.const import DEVICE_CLASS_ILLUMINANCE
from homeassistant.const import DEVICE_CLASS_TEMPERATURE
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import XTHL

from . import Sensor_EcoDevicesRT2


_LOGGER = logging.getLogger(__name__)


class Sensor_XTHL(Sensor_EcoDevicesRT2, Entity):
    """Representation of a X-THL sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self.control = XTHL(ecort2, self._id)
        self._device_class = device_class
        # Allow overriding of temperature unit if specified in the conf
        if device_class == DEVICE_CLASS_TEMPERATURE and not self._unit_of_measurement:
            self._unit_of_measurement = "°C"
        elif device_class == DEVICE_CLASS_HUMIDITY:
            self._unit_of_measurement = "%"
        elif device_class == DEVICE_CLASS_ILLUMINANCE:
            self._unit_of_measurement = "lx"


class Sensor_XTHL_Temp(Sensor_XTHL):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_TEMPERATURE, "Temperature")

    def _async_get_property(self):
        return self.control.temperature


class Sensor_XTHL_Hum(Sensor_XTHL):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_HUMIDITY, "Humidity")

    def _async_get_property(self):
        return self.control.humidity


class Sensor_XTHL_Lum(Sensor_XTHL):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_ILLUMINANCE, "Luminance")

    def _async_get_property(self):
        return self.control.luminosity
