from homeassistant.helpers.entity import Entity
from pyecodevices_rt2 import DigitalInput
from pyecodevices_rt2 import EcoDevicesRT2

from . import BinarySensor_EcoDevicesRT2


class BinarySensor_DigitalInput(BinarySensor_EcoDevicesRT2, Entity):
    """Representation of an BinarySensor_DigitalInput."""

    def __init__(
        self,
        device_config: dict,
        ecort2: EcoDevicesRT2,
    ):
        super().__init__(device_config, ecort2)
        self.control = DigitalInput(ecort2, self._id)

    def _async_get_status(self) -> bool:
        return self.control.status
