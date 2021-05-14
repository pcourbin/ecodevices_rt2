from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import EnOceanSwitch

from . import Switch_EcoDevicesRT2
from ..const import DEFAULT_ICON_SWITCH


class Switch_EnOcean(Switch_EcoDevicesRT2, Entity):
    """Representation of an EnOcean switch."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
    ):
        super().__init__(device_config, ecort2)
        self.control = EnOceanSwitch(ecort2, self._id)

        if not self._icon:
            self._icon = DEFAULT_ICON_SWITCH

    def _async_get_status(self, cached_ms: int = None) -> bool:
        return self.control.get_status(cached_ms=cached_ms)

    def _async_set_on(self) -> bool:
        return self.control.on()

    def _async_set_off(self) -> bool:
        return self.control.off()
