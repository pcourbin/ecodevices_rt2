"""Constants for the GCE Ecodevices RT2 component."""
DOMAIN = "ecodevices_rt2"

CONTROLLER = "controller"
CONFIG = "config"

UNDO_UPDATE_LISTENER = "undo_update_listener"
DEFAULT_CACHED_INTERVAL_MS = 1000
CONF_CACHED_INTERVAL_MS = "cached_interval_ms"
DEFAULT_UPDATE_AFTER_SWITCH = 0
CONF_UPDATE_AFTER_SWITCH = "update_after_switch"

DEFAULT_ICON_SWITCH = "mdi:toggle-switch"
DEFAULT_ICON_CURRENCY = "mdi:currency-eur"
DEFAULT_ICON_ENERGY = "mdi:flash"
DEFAULT_ICON_HEATER = "mdi:radiator"

PRESET_COMFORT_1 = "Comfort -1"
PRESET_COMFORT_2 = "Comfort -2"


CONF_API_RESPONSE_ENTRY = "status"
CONF_API_RESPONSE_SUCCESS_VALUE = "Success"
CONF_API_GET = "api_get"
CONF_API_GET_VALUE = "api_get_value"
CONF_API_GET_ENTRY = "api_get_entry"
CONF_API_ON_GET = "api_on_get"
CONF_API_ON_GET_VALUE = "api_on_get_value"
CONF_API_OFF_GET = "api_off_get"
CONF_API_OFF_GET_VALUE = "api_off_get_value"

CONF_DEVICES = "devices"
CONF_COMPONENT = "component"
CONF_TYPE = "type"
CONF_ID = "id"
CONF_SUBPOST_ID = "subpost"
CONF_ZONE_ID = "zone"
CONF_MODULE_ID = "module"

TYPE_API = "api"
TYPE_COUNTER = "counter"
TYPE_DIGITALLINPUT = "digitalinput"
TYPE_ENOCEAN = "enocean"
TYPE_POST = "post"
TYPE_RELAY = "relay"
TYPE_SUPPLIERINDEX = "supplierindex"
TYPE_TOROID = "toroid"
TYPE_VIRTUALOUTPUT = "virtualoutput"
TYPE_X4FP = "x4fp"
TYPE_XTHL = "xthl"

CONF_COMPONENT_ALLOWED = [
    "switch",
    "sensor",
    "climate",
    "binary_sensor",
    "light",
]

CONF_TYPE_COMPONENT_ALLOWED = {
    TYPE_API: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_API_GET, CONF_API_GET_VALUE, CONF_API_GET_ENTRY],
            "switch": [
                CONF_API_GET,
                CONF_API_GET_VALUE,
                CONF_API_GET_ENTRY,
                CONF_API_ON_GET,
                CONF_API_ON_GET_VALUE,
                CONF_API_OFF_GET,
                CONF_API_OFF_GET_VALUE,
            ],
            "light": [
                CONF_API_GET,
                CONF_API_GET_VALUE,
                CONF_API_GET_ENTRY,
                CONF_API_ON_GET,
                CONF_API_ON_GET_VALUE,
                CONF_API_OFF_GET,
                CONF_API_OFF_GET_VALUE,
            ],
        },
    },
    TYPE_COUNTER: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_ID],
        },
    },
    TYPE_DIGITALLINPUT: {
        "default": "binary_sensor",
        "parameters": {
            "binary_sensor": [CONF_ID],
        },
    },
    TYPE_ENOCEAN: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_ID],
            "switch": [CONF_ID],
            "light": [CONF_ID],
        },
    },
    TYPE_POST: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_ID],  # CONF_SUBPOST_ID
        },
    },
    TYPE_RELAY: {
        "default": "switch",
        "parameters": {
            "switch": [CONF_ID],
            "light": [CONF_ID],
        },
    },
    TYPE_SUPPLIERINDEX: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_ID],
        },
    },
    TYPE_TOROID: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_ID],
        },
    },
    TYPE_VIRTUALOUTPUT: {
        "default": "switch",
        "parameters": {
            "switch": [CONF_ID],
            "light": [CONF_ID],
        },
    },
    TYPE_X4FP: {
        "default": "climate",
        "parameters": {
            "climate": [CONF_MODULE_ID, CONF_ZONE_ID],
            "switch": [CONF_MODULE_ID, CONF_ZONE_ID],
        },
    },
    TYPE_XTHL: {
        "default": "sensor",
        "parameters": {
            "sensor": [CONF_ID],
        },
    },
}
