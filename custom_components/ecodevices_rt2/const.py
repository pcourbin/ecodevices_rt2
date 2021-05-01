"""Constants for the EcoDevices component."""
DOMAIN = "ecodevices_rt2"

CONTROLLER = "controller"
CONFIG = "config"
PLATFORMS = ["sensor", "switch", "climate"]
UNDO_UPDATE_LISTENER = "undo_update_listener"

RT2_RESPONSE_ENTRY = "status"
RT2_RESPONSE_SUCCESS_VALUE = "Success"

CONF_RT2_COMMAND = "rt2_command"
CONF_RT2_COMMAND_VALUE = "rt2_command_value"
CONF_RT2_COMMAND_ENTRY = "rt2_command_entry"
CONF_RT2_ON_COMMAND = "rt2_on_command"
CONF_RT2_ON_COMMAND_VALUE = "rt2_on_command_value"
CONF_RT2_OFF_COMMAND = "rt2_off_command"
CONF_RT2_OFF_COMMAND_VALUE = "rt2_off_command_value"

RT2_FP_GET_COMMAND = "Get"
RT2_FP_GET_COMMAND_VALUE = "FP"
RT2_FP_GET_COMMAND_ENTRY = "FP%s Zone %s"
RT2_FP_SET_COMMAND = "SetFP0%s"

CONF_RT2_FP_EXT = "rt2_fp_ext"
CONF_RT2_FP_ZONE = "rt2_fp_zone"