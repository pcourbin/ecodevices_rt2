import logging

from homeassistant.components.sensor import DEVICE_CLASS_UNITS
from homeassistant.components.sensor import SensorDeviceClass
from homeassistant.components.sensor import SensorEntity
from homeassistant.components.sensor import SensorStateClass
from homeassistant.const import UnitOfEnergy
from homeassistant.const import UnitOfPower
from homeassistant.const import UnitOfTemperature
from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import UNDEFINED
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util.unit_system import METRIC_SYSTEM
from pyecodevices_rt2 import EcoDevicesRT2

from ..const import CONF_ALLOW_ZERO
from ..const import CONF_ICON_HUMIDITY
from ..const import CONF_ICON_ILLUMINANCE
from ..const import CONF_ICON_INDEX
from ..const import CONF_ICON_INSTANT
from ..const import CONF_ICON_PRICE
from ..const import CONF_ICON_TEMPERATURE
from ..const import CONF_UNIT_HUMIDITY
from ..const import CONF_UNIT_ILLUMINANCE
from ..const import CONF_UNIT_INDEX
from ..const import CONF_UNIT_INSTANT
from ..const import CONF_UNIT_PRICE
from ..const import CONF_UNIT_TEMPERATURE
from ..device_ecodevicesrt2 import EcoDevicesRT2Device

# from homeassistant.components.sensor import CONF_STATE_CLASS
CONF_STATE_CLASS = "state_class"

_LOGGER = logging.getLogger(__name__)


def update_unit_icon(
    entity: SensorEntity, device_config: dict, conf_unit, default_unit, conf_icon
):
    if not entity._unit_of_measurement:
        entity._unit_of_measurement = default_unit
        if device_config.get(conf_unit):
            entity._unit_of_measurement = device_config.get(conf_unit)
    if not entity._icon and device_config.get(conf_icon):
        entity._icon = device_config.get(conf_icon)


class Sensor_EcoDevicesRT2(EcoDevicesRT2Device, SensorEntity):
    def __init__(
        self,
        hass: HomeAssistant,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        device_class: str = "",
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        self._allow_zero = device_config.get(CONF_ALLOW_ZERO, True)
        self._state = None
        self._state_class = device_config.get(CONF_STATE_CLASS)

        if device_class == "" and self._device_class:
            device_class = self._device_class

        if device_class != "":
            if device_class in DEVICE_CLASS_UNITS:
                default_unit = list(DEVICE_CLASS_UNITS[device_class])[0]
            else:
                default_unit = UNDEFINED
            self._device_class = device_class
            if device_class == SensorDeviceClass.MONETARY:
                update_unit_icon(
                    self,
                    device_config,
                    CONF_UNIT_PRICE,
                    hass.config.currency,
                    CONF_ICON_PRICE,
                )
                self._state_class = SensorStateClass.TOTAL_INCREASING
            elif device_class == SensorDeviceClass.ENERGY:
                update_unit_icon(
                    self,
                    device_config,
                    CONF_UNIT_INDEX,
                    UnitOfEnergy.WATT_HOUR,
                    CONF_ICON_INDEX,
                )
                self._state_class = SensorStateClass.TOTAL_INCREASING
            elif device_class == SensorDeviceClass.POWER:
                update_unit_icon(
                    self,
                    device_config,
                    CONF_UNIT_INSTANT,
                    UnitOfPower.WATT,
                    CONF_ICON_INSTANT,
                )
                self._state_class = SensorStateClass.MEASUREMENT
            elif device_class == SensorDeviceClass.TEMPERATURE:
                if hass.config.units == METRIC_SYSTEM:
                    default_unit = UnitOfTemperature.CELSIUS
                else:
                    default_unit = UnitOfTemperature.FAHRENHEIT

                update_unit_icon(
                    self,
                    device_config,
                    CONF_UNIT_TEMPERATURE,
                    default_unit,
                    CONF_ICON_TEMPERATURE,
                )
                self._state_class = SensorStateClass.MEASUREMENT
            elif device_class == SensorDeviceClass.HUMIDITY:
                update_unit_icon(
                    self,
                    device_config,
                    CONF_UNIT_HUMIDITY,
                    default_unit,
                    CONF_ICON_HUMIDITY,
                )
                self._state_class = SensorStateClass.MEASUREMENT
            elif device_class == SensorDeviceClass.ILLUMINANCE:
                update_unit_icon(
                    self,
                    device_config,
                    CONF_UNIT_ILLUMINANCE,
                    default_unit,
                    CONF_ICON_ILLUMINANCE,
                )
                self._state_class = SensorStateClass.MEASUREMENT
            else:
                if not self._unit_of_measurement:
                    self._unit_of_measurement = default_unit

    @property
    def state(self) -> str:
        """Return the state."""
        try:
            self._state = self.get_property()
            self._available = True
        except Exception as e:
            _LOGGER.error("Device data no retrieve %s: %s", self.name, e)
            self._available = False
        return self._state

    def get_property(self, cached_ms: int = None) -> bool:
        pass

    @property
    def state_class(self) -> str:
        """Return the state class."""
        return self._state_class
