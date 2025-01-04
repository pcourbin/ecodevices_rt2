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
from ..const import CONF_STATE_CLASS
from ..const import CONF_UNIT_HUMIDITY
from ..const import CONF_UNIT_ILLUMINANCE
from ..const import CONF_UNIT_INDEX
from ..const import CONF_UNIT_INSTANT
from ..const import CONF_UNIT_PRICE
from ..const import CONF_UNIT_TEMPERATURE
from ..device_ecodevicesrt2 import EcoDevicesRT2Device

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
        suffix_name: str = "",
    ):
        super().__init__(device_config, ecort2, coordinator, suffix_name)
        self._allow_zero = device_config.get(CONF_ALLOW_ZERO, True)
        self._state = None
        self._state_class = device_config.get(CONF_STATE_CLASS)

        if self._device_class != "":
            if self._device_class in DEVICE_CLASS_UNITS:
                default_unit = list(DEVICE_CLASS_UNITS[self._device_class])[0]
            else:
                default_unit = UNDEFINED

            conf_unit = UNDEFINED
            conf_icon = UNDEFINED

            if self._device_class == SensorDeviceClass.MONETARY:
                default_unit = hass.config.currency
                conf_unit = CONF_UNIT_PRICE
                conf_icon = CONF_ICON_PRICE
            elif self._device_class == SensorDeviceClass.TEMPERATURE:
                if hass.config.units == METRIC_SYSTEM:
                    default_unit = UnitOfTemperature.CELSIUS
                else:
                    default_unit = UnitOfTemperature.FAHRENHEIT
                conf_unit = CONF_UNIT_TEMPERATURE
                conf_icon = CONF_ICON_TEMPERATURE
            elif self._device_class == SensorDeviceClass.HUMIDITY:
                conf_unit = CONF_UNIT_HUMIDITY
                conf_icon = CONF_ICON_HUMIDITY
            elif self._device_class == SensorDeviceClass.ILLUMINANCE:
                conf_unit = CONF_UNIT_ILLUMINANCE
                conf_icon = CONF_ICON_ILLUMINANCE
            elif self._device_class == SensorDeviceClass.ENERGY:
                default_unit = UnitOfEnergy.WATT_HOUR  # default_unit
                conf_unit = CONF_UNIT_INDEX
                conf_icon = CONF_ICON_INDEX
            elif self._device_class == SensorDeviceClass.POWER:
                default_unit = UnitOfPower.WATT  # default_unit
                conf_unit = CONF_UNIT_INSTANT
                conf_icon = CONF_ICON_INSTANT
            elif self._state_class == SensorStateClass.MEASUREMENT:
                conf_unit = CONF_UNIT_INSTANT
                conf_icon = CONF_ICON_INSTANT
            elif self._state_class == SensorStateClass.TOTAL_INCREASING:
                conf_unit = CONF_UNIT_INDEX
                conf_icon = CONF_ICON_INDEX

            update_unit_icon(
                self,
                device_config,
                conf_unit,
                default_unit,
                conf_icon,
            )

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
