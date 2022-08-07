from homeassistant.components.sensor import STATE_CLASS_MEASUREMENT
from homeassistant.components.sensor import STATE_CLASS_TOTAL_INCREASING
from homeassistant.const import DEVICE_CLASS_ENERGY
from homeassistant.const import DEVICE_CLASS_MONETARY
from homeassistant.const import DEVICE_CLASS_POWER
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import Post

from . import Sensor_EcoDevicesRT2
from ..const import CONF_SUBPOST_ID
from ..const import DEFAULT_ICON_CURRENCY
from ..const import DEFAULT_ICON_ENERGY


class Sensor_Post(Sensor_EcoDevicesRT2):
    """Representation of an Post_Sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        device_class: str,
        suffix_name: str,
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        if CONF_SUBPOST_ID in device_config:
            self.control = Post(ecort2, self._id, device_config[CONF_SUBPOST_ID])
        else:
            self.control = Post(ecort2, self._id)
        self._device_class = device_class
        # Allow overriding of currency unit and icon if specified in the conf
        if device_class == DEVICE_CLASS_MONETARY:
            if not self._unit_of_measurement:
                self._unit_of_measurement = "€"
            if not self._icon:
                self._icon = DEFAULT_ICON_CURRENCY
            self._state_class = STATE_CLASS_TOTAL_INCREASING
        elif device_class == DEVICE_CLASS_ENERGY:
            self._unit_of_measurement = "kWh"
            self._icon = DEFAULT_ICON_ENERGY
            self._state_class = STATE_CLASS_TOTAL_INCREASING
        elif device_class == DEVICE_CLASS_POWER:
            self._unit_of_measurement = "W"
            self._icon = DEFAULT_ICON_ENERGY
            self._state_class = STATE_CLASS_MEASUREMENT


class Sensor_Post_Index(Sensor_Post):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            device_config, ecort2, coordinator, DEVICE_CLASS_ENERGY, "Index"
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_index(cached_ms)
        if value is not None and float(value) > 0:
            return value


class Sensor_Post_Price(Sensor_Post):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            device_config, ecort2, coordinator, DEVICE_CLASS_MONETARY, "Price"
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_price(cached_ms)
        if value is not None and float(value) > 0:
            return value


class Sensor_Post_IndexDay(Sensor_Post):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            device_config, ecort2, coordinator, DEVICE_CLASS_ENERGY, "IndexDay"
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_index_day(cached_ms)
        if value is not None and float(value) > 0:
            return value


class Sensor_Post_PriceDay(Sensor_Post):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            device_config, ecort2, coordinator, DEVICE_CLASS_MONETARY, "PriceDay"
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_price_day(cached_ms)
        if value is not None and float(value) > 0:
            return value


class Sensor_Post_Instant(Sensor_Post):
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(
            device_config, ecort2, coordinator, DEVICE_CLASS_POWER, "Instant"
        )

    def get_property(self, cached_ms: int = None):
        value = self.control.get_instant(cached_ms)
        if value is not None and float(value) > 0:
            return value
