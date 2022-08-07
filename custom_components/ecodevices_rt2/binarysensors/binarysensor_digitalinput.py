from homeassistant.helpers.entity import Entity
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator
from pyecodevices_rt2 import DigitalInput
from pyecodevices_rt2 import EcoDevicesRT2

from . import BinarySensor_EcoDevicesRT2


class BinarySensor_DigitalInput(BinarySensor_EcoDevicesRT2, Entity):
    """Representation of an BinarySensor_DigitalInput."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
        coordinator: DataUpdateCoordinator,
    ):
        super().__init__(device_config, ecort2, coordinator)
        self.control = DigitalInput(ecort2, self._id)

    def get_status(self) -> bool:
        return self.control.status
