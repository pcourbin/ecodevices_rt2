import re

from homeassistant.const import CONF_DEVICE_CLASS
from homeassistant.const import CONF_ICON
from homeassistant.const import CONF_NAME
from homeassistant.const import CONF_UNIT_OF_MEASUREMENT
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2

from .const import CONF_COMPONENT
from .const import CONF_ID
from .const import CONF_SUBPOST_ID
from .const import CONF_TYPE
from .const import CONF_ZONE_ID
from .const import DOMAIN


class EcoDevicesRT2Device(CoordinatorEntity):
    """Representation of a GCE Ecodevices RT2 generic device entity."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        suffix_name: str = "",
    ):
        """Initialize the device."""
        super().__init__(coordinator)

        self.ecort2 = ecort2

        self._name = device_config.get(CONF_NAME)
        self._device_name = self._name
        if suffix_name:
            self._name += f" {suffix_name}"

        self._device_class = device_config.get(CONF_DEVICE_CLASS)
        self._unit_of_measurement = device_config.get(CONF_UNIT_OF_MEASUREMENT)
        self._icon = device_config.get(CONF_ICON)
        self._ecort2_type = device_config.get(CONF_TYPE)
        self._component = device_config.get(CONF_COMPONENT)
        self._id = device_config.get(CONF_ID)
        self._zone_id = device_config.get(CONF_ZONE_ID, "")
        self._subpost_id = device_config.get(CONF_SUBPOST_ID, "")

        self._supported_features = 0

    @property
    def name(self):
        """Return the display name."""
        return self._name

    @property
    def unique_id(self):
        """Return an unique id."""
        return "_".join(
            [
                DOMAIN,
                self.ecort2.host,
                self._component,
                re.sub("[^A-Za-z0-9_]+", "", self._name.replace(" ", "_")).lower(),
            ]
        )

    @property
    def device_info(self):
        """Return device info."""
        return {
            "identifiers": {
                (
                    DOMAIN,
                    re.sub(
                        "[^A-Za-z0-9_]+", "", self._device_name.replace(" ", "_")
                    ).lower(),
                )
            },
            "name": self._device_name,
            "manufacturer": "GCE",
            "model": "Ecodevices RT2",
            "via_device": (DOMAIN, self.ecort2.host),
        }

    @property
    def icon(self):
        """Icon to use in the frontend, if any."""
        return self._icon

    @property
    def device_class(self):
        """Return the device class."""
        return self._device_class

    @property
    def unit_of_measurement(self):
        """Return the unit of measurement."""
        return self._unit_of_measurement
