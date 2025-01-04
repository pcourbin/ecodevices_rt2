from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorStateClass
from homeassistant.core import HomeAssistant
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import SupplierIndex

from . import Sensor_EcoDevicesRT2
from ..const import CONF_DEVICE_CLASS
from ..const import CONF_STATE_CLASS


class Sensor_SupplierIndex(Sensor_EcoDevicesRT2):
    """Representation of an SupplierIndex sensor."""

    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        suffix_name: str,
    ):
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            suffix_name,
        )
        self.control = SupplierIndex(ecort2, self._id)


class Sensor_SupplierIndex_Index(Sensor_SupplierIndex):
    def __init__(
        self,
        hass: HomeAssistant,
        device_config_g: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        device_config = dict(device_config_g)
        if CONF_DEVICE_CLASS not in device_config:
            device_config[CONF_DEVICE_CLASS] = SensorDeviceClass.ENERGY
        device_config[CONF_STATE_CLASS] = SensorStateClass.TOTAL_INCREASING
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
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
        device_config_g: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        device_config = dict(device_config_g)
        device_config[CONF_DEVICE_CLASS] = SensorDeviceClass.MONETARY
        device_config[CONF_STATE_CLASS] = SensorStateClass.TOTAL_INCREASING
        super().__init__(
            hass,
            device_config,
            ecort2,
            coordinator,
            "Price",
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_price(cached_ms)
        if value is not None and (self._allow_zero or float(value) != 0):
            return value
