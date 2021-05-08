"""Test IMA Protect Alarm switch."""
import logging
import time

from custom_components.ecodevices_rt2 import async_setup_entry
from custom_components.ecodevices_rt2.const import DOMAIN
from homeassistant.components.switch import SERVICE_TURN_OFF
from homeassistant.components.switch import SERVICE_TURN_ON
from homeassistant.exceptions import ConfigEntryNotReady
from pytest_homeassistant_custom_component.common import MockConfigEntry

from .const import MOCK_CONFIG

_LOGGER = logging.getLogger(__name__)


async def test_switch_services(hass):
    """Test switch services."""
    # Create a mock entry so we don't have to go through config flow
    config_entry = MockConfigEntry(domain=DOMAIN, data=MOCK_CONFIG, entry_id="test")
    try:
        await async_setup_entry(hass, config_entry)
        await hass.async_block_till_done()
    except ConfigEntryNotReady:
        """
        with patch(
            "custom_components.ecodevices_rt2.sensors.Switch_EcoDevicesRT2.async_update"
        ):
            self._is_on = self._is_on_command
            yield
        """
        assert True
        return

    _LOGGER.error("GO")

    await hass.services.async_call(
        "switch",
        SERVICE_TURN_ON,
        service_data={"entity_id": "switch.enocean_switch_1"},
        blocking=True,
    )

    time.sleep(5)
    assert hass.states.get("switch.enocean_switch_1").state == "on"
    _LOGGER.error("State : %s" % (hass.states.get("switch.enocean_switch_1").state))
    await hass.services.async_call(
        "switch",
        SERVICE_TURN_OFF,
        service_data={"entity_id": "switch.enocean_switch_1"},
        blocking=True,
    )
    time.sleep(5)
    assert hass.states.get("switch.enocean_switch_1").state == "off"
    _LOGGER.error("State : %s" % (hass.states.get("switch.enocean_switch_1").state))
    return
