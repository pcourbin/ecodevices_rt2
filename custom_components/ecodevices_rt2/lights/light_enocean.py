from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import EnOceanSwitch

from . import Light_EcoDevicesRT2


class Light_EnOcean(Light_EcoDevicesRT2, Entity):
    """Representation of an EnOcean switch."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
    ):
        super().__init__(device_config, ecort2)
        self.control = EnOceanSwitch(ecort2, self._id)

    def _async_get_status(self) -> bool:
        return self.control.status

    def _async_set_on(self) -> bool:
        return self.control.on()

    def _async_set_off(self) -> bool:
        return self.control.off()