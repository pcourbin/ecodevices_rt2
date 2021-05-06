"""Get information from GCE Ecodevices RT2."""
from .switch_ecodevicesrt2 import Switch_EcoDevicesRT2  # noreorder
from .switch_api import Switch_API
from .switch_enocean import Switch_EnOcean
from .switch_relay import Switch_Relay
from .switch_virtualoutput import Switch_VirtualOutput
from .switch_x4fp import Switch_X4FP

__all__ = [
    "Switch_EcoDevicesRT2",
    "Switch_EnOcean",
    "Switch_API",
    "Switch_Relay",
    "Switch_VirtualOutput",
    "Switch_X4FP",
]
