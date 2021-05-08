"""Global fixtures for GCE Ecodevices RT2 integration."""
from unittest.mock import patch

import pytest

pytest_plugins = "pytest_homeassistant_custom_component"


# This fixture is used to prevent HomeAssistant from attempting to create and dismiss persistent
# notifications. These calls would fail without this fixture since the persistent_notification
# integration is never loaded during a test.
@pytest.fixture(name="skip_notifications", autouse=True)
def skip_notifications_fixture():
    """Skip notification calls."""
    with patch("homeassistant.components.persistent_notification.async_create"), patch(
        "homeassistant.components.persistent_notification.async_dismiss"
    ):
        yield


@pytest.fixture
def bypass_sensor_async_update():
    with patch(
        "custom_components.ecodevices_rt2.sensors.Sensor_EcoDevicesRT2.async_update"
    ):
        yield


# This fixture, when used, will result in calls to async_get_data to return None. To have the call
# return a value, we would add the `return_value=<VALUE_TO_RETURN>` parameter to the patch call.
@pytest.fixture(name="bypass_get_data")
def bypass_get_data_fixture(bypass_sensor_async_update):
    """Skip calls to get data from Ecodevices RT2 API."""
    with patch("pyecodevices_rt2.EcoDevicesRT2.ping", return_value=True):
        yield
    """
    with patch(
        "custom_components.ecodevices_rt2.lights.Light_EcoDevicesRT2.async_update"
    ):
        with patch(
            "custom_components.ecodevices_rt2.climates.Climate_X4FP.async_update"
        ):
            with patch(
                "custom_components.ecodevices_rt2.binarysensors.BinarySensor_EcoDevicesRT2.async_update"
            ):
                with patch(
                    "custom_components.ecodevices_rt2.switches.Switch_EcoDevicesRT2.async_update"
                ):
    """


# In this fixture, we are forcing calls to async_get_data to raise an Exception. This is useful
# for exception handling.
@pytest.fixture(name="error_on_connect")
def error_on_connect_fixture():
    """Simulate error when retrieving data from API."""
    with patch(
        "pyecodevices_rt2.EcoDevicesRT2.ping",
        side_effect=Exception,
    ):
        yield


@pytest.fixture(name="error_on_connect_ping")
def error_on_connect_ping_fixture():
    """Simulate error when retrieving data from API."""
    with patch("pyecodevices_rt2.EcoDevicesRT2.ping", return_value=False):
        yield
