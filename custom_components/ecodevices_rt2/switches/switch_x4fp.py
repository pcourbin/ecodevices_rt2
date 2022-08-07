from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import X4FP

from . import Switch_EcoDevicesRT2
from ..const import DEFAULT_ICON_HEATER


class Switch_X4FP(Switch_EcoDevicesRT2, Entity):
    """Representation of an X4FP switch."""

    # ON -> CONFORT MODE == 0
    # OFF -> NONE MODE == 3
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
        module_id: int,
        zone_id: int,
    ):
        super().__init__(device_config, ecort2, coordinator)
        self._module_id = module_id
        self._zone_id = zone_id
        self.control = X4FP(ecort2, self._module_id, self._zone_id)

        if not self._icon:
            self._icon = DEFAULT_ICON_HEATER

    def get_status(self, cached_ms: int = None) -> bool:
        return self.control.get_mode(cached_ms=cached_ms) == 0

    def set_on(self) -> bool:
        self.control.mode = 0
        return True

    def set_off(self) -> bool:
        self.control.mode = 3
        return True
