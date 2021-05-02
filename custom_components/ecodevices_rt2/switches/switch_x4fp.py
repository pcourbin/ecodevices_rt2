from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import X4FP

from . import Switch_EcoDevicesRT2


class Switch_X4FP(Switch_EcoDevicesRT2, Entity):
    """Representation of an X4FP switch."""

    # ON -> CONFORT MODE == 0
    # OFF -> NONE MODE == 3
    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        module_id: int,
        zone_id: int,
    ):
        super().__init__(device_config, ecort2)
        self._module_id = module_id
        self._zone_id = zone_id
        self.control = X4FP(ecort2, self._module_id, self._zone_id)

    def _async_get_status(self) -> bool:
        return self.control.mode == 0

    def _async_set_on(self) -> bool:
        self.control.mode = 0
        return True

    def _async_set_off(self) -> bool:
        self.control.mode = 3
        return True
