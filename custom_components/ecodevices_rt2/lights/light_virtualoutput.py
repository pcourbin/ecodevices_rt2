from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import EcoDevicesRT2
from pyecodevices_rt2 import VirtualOutput

from . import Light_EcoDevicesRT2


class Light_VirtualOutput(Light_EcoDevicesRT2, Entity):
    """Representation of an VirtualOutput switch."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(device_config, ecort2, coordinator)
        self.control = VirtualOutput(ecort2, self._id)

    def get_status(self, cached_ms: int = None) -> bool:
        return self.control.get_status(cached_ms=cached_ms)

    def set_on(self) -> bool:
        return self.control.on()

    def set_off(self) -> bool:
        return self.control.off()
