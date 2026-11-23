"""Apply a generic model override to the Ecovacs integration.

This integration adds no platforms, entities, services or config flow. It exists
only to install one narrowly scoped override into ``deebot_client`` at import
time: one cloud hardware class is resolved with a different existing static
capability profile. Every other hardware class keeps its original behaviour.

Add ``ecovacs_model_override:`` to configuration.yaml so Home Assistant loads
this module at bootstrap, before the Ecovacs config entries initialise devices.
"""

from __future__ import annotations

import deebot_client.hardware as _hardware

from homeassistant.core import HomeAssistant
from homeassistant.helpers.typing import ConfigType

# --- Verified model override mapping: kept unchanged ---
_original_get_static_device_info = _hardware.get_static_device_info

async def _get_static_device_info(class_: str):
    if class_ == "4jd37g":
        class_ = "mxse7w"
    return await _original_get_static_device_info(class_)

_hardware.get_static_device_info = _get_static_device_info

from deebot_client import api_client as _api_client
_api_client.get_static_device_info = _get_static_device_info
# --- End verified model override mapping ---


async def async_setup(hass: HomeAssistant, config: ConfigType) -> bool:
    """Load the patch; it is already applied when this module is imported."""
    return True
