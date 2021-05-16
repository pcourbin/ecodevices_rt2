from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2

from . import Switch_EcoDevicesRT2
from ..const import CONF_API_RESPONSE_ENTRY
from ..const import CONF_API_RESPONSE_SUCCESS_VALUE
from ..const import DEFAULT_ICON_SWITCH


class Switch_API(Switch_EcoDevicesRT2, Entity):
    """Representation of an EnOcean sensor."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        get,
        get_value,
        get_entry,
        on_get,
        on_get_value,
        off_get,
        off_get_value,
    ):
        super().__init__(device_config, ecort2, coordinator)
        self._get = get
        self._get_value = get_value
        self._get_entry = get_entry
        # Add Call to cached value in ecort2
        ecort2._cached[self._get + "=" + self._get_value] = {}

        self._on_get = on_get
        self._on_get_value = on_get_value
        self._off_get = off_get
        self._off_get_value = off_get_value

        if not self._icon:
            self._icon = DEFAULT_ICON_SWITCH

    def get_status(self, cached_ms: int = None) -> bool:
        return (
            self.ecort2.get(
                self._get, self._get_value, self._get_entry, cached_ms=cached_ms
            )
            == 1
        )

    def set_on(self) -> bool:
        api_response = self.ecort2.get(
            self._on_get, self._on_get_value, CONF_API_RESPONSE_ENTRY
        )
        return api_response == CONF_API_RESPONSE_SUCCESS_VALUE

    def set_off(self) -> bool:
        api_response = self.ecort2.get(
            self._off_get, self._off_get_value, CONF_API_RESPONSE_ENTRY
        )
        return api_response == CONF_API_RESPONSE_SUCCESS_VALUE
