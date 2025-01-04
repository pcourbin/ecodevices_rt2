from homeassistant.const import CONF_DEVICE_CLASS
from homeassistant.const import CONF_ICON
from homeassistant.const import CONF_NAME
from homeassistant.const import CONF_UNIT_OF_MEASUREMENT
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from homeassistant.util import slugify
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

        self._attr_name: str = device_config[CONF_NAME]
        if suffix_name:
            self._attr_name = f"{self._attr_name} {suffix_name}"

        self._device_class = device_config.get(CONF_DEVICE_CLASS)
        self._unit_of_measurement = device_config.get(CONF_UNIT_OF_MEASUREMENT)
        self._icon = device_config.get(CONF_ICON)
        self._ecort2_type = device_config.get(CONF_TYPE)
        self._component = device_config.get(CONF_COMPONENT)
        self._id = device_config.get(CONF_ID)

        self._zone_id = device_config.get(CONF_ZONE_ID, "")
        self._subpost_id = device_config.get(CONF_SUBPOST_ID, "")

        self._supported_features = 0

        self._configuration_url = f"http://{self.ecort2.host}:{self.ecort2.port}"

        self._attr_unique_id = "_".join(
            [DOMAIN, self.ecort2.host, self._component, slugify(self._attr_name)]
        )

        self._attr_device_info = {
            "identifiers": {(DOMAIN, slugify(device_config[CONF_NAME]))},
            "name": device_config[CONF_NAME],
            "manufacturer": "GCE",
            "model": "Ecodevices RT2",
            "via_device": (DOMAIN, self.ecort2.host),
            "configuration_url": self._configuration_url,
        }
