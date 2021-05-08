"""Constants for GCE Ecodevices RT2 tests."""
import os

from custom_components.ecodevices_rt2.const import CONF_API_GET
from custom_components.ecodevices_rt2.const import CONF_API_GET_ENTRY
from custom_components.ecodevices_rt2.const import CONF_API_GET_VALUE
from custom_components.ecodevices_rt2.const import CONF_API_OFF_GET
from custom_components.ecodevices_rt2.const import CONF_API_OFF_GET_VALUE
from custom_components.ecodevices_rt2.const import CONF_API_ON_GET
from custom_components.ecodevices_rt2.const import CONF_API_ON_GET_VALUE
from custom_components.ecodevices_rt2.const import CONF_COMPONENT
from custom_components.ecodevices_rt2.const import CONF_DEVICES
from custom_components.ecodevices_rt2.const import CONF_ID
from custom_components.ecodevices_rt2.const import CONF_MODULE_ID
from custom_components.ecodevices_rt2.const import CONF_SUBPOST_ID
from custom_components.ecodevices_rt2.const import CONF_TYPE
from custom_components.ecodevices_rt2.const import CONF_ZONE_ID
from custom_components.ecodevices_rt2.const import TYPE_API
from custom_components.ecodevices_rt2.const import TYPE_COUNTER
from custom_components.ecodevices_rt2.const import TYPE_DIGITALINPUT
from custom_components.ecodevices_rt2.const import TYPE_ENOCEAN
from custom_components.ecodevices_rt2.const import TYPE_POST
from custom_components.ecodevices_rt2.const import TYPE_RELAY
from custom_components.ecodevices_rt2.const import TYPE_SUPPLIERINDEX
from custom_components.ecodevices_rt2.const import TYPE_TOROID
from custom_components.ecodevices_rt2.const import TYPE_VIRTUALOUTPUT
from custom_components.ecodevices_rt2.const import TYPE_X4FP
from custom_components.ecodevices_rt2.const import TYPE_XTHL
from dotenv import load_dotenv
from homeassistant.const import CONF_API_KEY
from homeassistant.const import CONF_DEVICE_CLASS
from homeassistant.const import CONF_HOST
from homeassistant.const import CONF_ICON
from homeassistant.const import CONF_NAME
from homeassistant.const import CONF_PORT
from homeassistant.const import CONF_SCAN_INTERVAL
from homeassistant.const import CONF_UNIT_OF_MEASUREMENT

load_dotenv()

MOCK_CONFIG = {
    CONF_HOST: os.environ.get("ECORT2_HOST", ""),
    CONF_PORT: os.environ.get("ECORT2_PORT", 80),
    CONF_API_KEY: os.environ.get("ECORT2_APIKEY", ""),
    CONF_SCAN_INTERVAL: 15,
    CONF_NAME: "EcoRT2",
    CONF_DEVICES: [
        {
            CONF_NAME: "Elec Index HC (from API)",
            CONF_TYPE: TYPE_API,
            CONF_COMPONENT: "sensor",
            CONF_API_GET: "Index",
            CONF_API_GET_VALUE: "All",
            CONF_API_GET_ENTRY: "Index_TI1",
            CONF_DEVICE_CLASS: "power",
            CONF_UNIT_OF_MEASUREMENT: "kWh",
            CONF_ICON: "mdi:flash",
        },
        {
            CONF_NAME: "EnOcean Switch 1 (from API)",
            CONF_TYPE: TYPE_API,
            CONF_COMPONENT: "switch",
            CONF_API_GET: "Get",
            CONF_API_GET_VALUE: "XENO",
            CONF_API_GET_ENTRY: "ENO ACTIONNEUR1",
            CONF_API_ON_GET: "SetEnoPC",
            CONF_API_ON_GET_VALUE: "1",
            CONF_API_OFF_GET: "ClearEnoPC",
            CONF_API_OFF_GET_VALUE: "SetEnoPC",
        },
        {
            CONF_NAME: "Counter 1",
            CONF_TYPE: TYPE_COUNTER,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "DigitalInput 1",
            CONF_TYPE: TYPE_DIGITALINPUT,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "EnOcean Sensor 1",
            CONF_TYPE: TYPE_ENOCEAN,
            CONF_ID: 1,
            CONF_UNIT_OF_MEASUREMENT: "°C",
            CONF_ICON: "mdi:thermometer",
        },
        {
            CONF_NAME: "EnOcean Switch 1",
            CONF_TYPE: TYPE_ENOCEAN,
            CONF_COMPONENT: "switch",
            CONF_ID: 1,
        },
        {
            CONF_NAME: "EnOcean Switch 2 as Light",
            CONF_TYPE: TYPE_ENOCEAN,
            CONF_COMPONENT: "light",
            CONF_ID: 2,
        },
        {
            CONF_NAME: "Post 1",
            CONF_TYPE: TYPE_POST,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "Subpost 2 of Post 1",
            CONF_TYPE: TYPE_POST,
            CONF_ID: 1,
            CONF_SUBPOST_ID: 2,
        },
        {
            CONF_NAME: "Relay 1",
            CONF_TYPE: TYPE_RELAY,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "Relay 2 as Light",
            CONF_TYPE: TYPE_RELAY,
            CONF_COMPONENT: "light",
            CONF_ID: 2,
        },
        {
            CONF_NAME: "Supplier Index 1 (EDF Info)",
            CONF_TYPE: TYPE_SUPPLIERINDEX,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "Toroid 1",
            CONF_TYPE: TYPE_TOROID,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "Toroid 5",
            CONF_TYPE: TYPE_TOROID,
            CONF_ID: 5,
        },
        {
            CONF_NAME: "Virtual Output 1",
            CONF_TYPE: TYPE_VIRTUALOUTPUT,
            CONF_ID: 1,
        },
        {
            CONF_NAME: "Virtual Output 2 as Light",
            CONF_TYPE: TYPE_VIRTUALOUTPUT,
            CONF_COMPONENT: "light",
            CONF_ID: 2,
        },
        {
            CONF_NAME: "Heater Module 1 Zone 1",
            CONF_TYPE: TYPE_X4FP,
            CONF_MODULE_ID: 1,
            CONF_ZONE_ID: 1,
        },
        {
            CONF_NAME: "Heater Module 1 Zone 1",
            CONF_TYPE: TYPE_X4FP,
            CONF_COMPONENT: "switch",
            CONF_MODULE_ID: 1,
            CONF_ZONE_ID: 2,
        },
        {
            CONF_NAME: "XHTL 1",
            CONF_TYPE: TYPE_XTHL,
            CONF_ID: 1,
        },
    ],
}
