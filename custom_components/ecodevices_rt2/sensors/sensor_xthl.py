from homeassistant.const import DEVICE_CLASS_HUMIDITY
from homeassistant.const import DEVICE_CLASS_ILLUMINANCE
from homeassistant.const import DEVICE_CLASS_TEMPERATURE
from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import XTHL

from . import Sensor_EcoDevicesRT2


class Sensor_XTHL(Sensor_EcoDevicesRT2, Entity):
    """Representation of a X-THL sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        device_class: str,
        unit_of_measurement: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, suffix_name)
        self.control = XTHL(ecort2, self._id)
        self._device_class = device_class
        # Allow overriding of temperature unit if specified in the xthl conf
        if not (self._unit_of_measurement and device_class == DEVICE_CLASS_TEMPERATURE):
            self._unit_of_measurement = unit_of_measurement


class Sensor_XTHL_Temp(Sensor_XTHL):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(
            device_config, ecort2, DEVICE_CLASS_TEMPERATURE, "°C", "Temperature"
        )

    def _async_get_property(self):
        return self.control.temperature


class Sensor_XTHL_Hum(Sensor_XTHL):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(device_config, ecort2, DEVICE_CLASS_HUMIDITY, "%", "Humidity")

    def _async_get_property(self):
        return self.control.humidity


class Sensor_XTHL_Lum(Sensor_XTHL):
    def __init__(self, device_config: dict, ecort2: EcoDevicesRT2):
        super().__init__(
            device_config, ecort2, DEVICE_CLASS_ILLUMINANCE, "lx", "Luminance"
        )

    def _async_get_property(self):
        return self.control.luminosity
