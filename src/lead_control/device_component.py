from typing import Dict

from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import (
    control_list,
    MappedControl
)
from ableton.v3.live import get_parameter_by_name
from ableton.v3.live.action import toggle_or_cycle_parameter_value

from .logging import log_function_call, LOGGER
from .tag import LeadControlTag


class DeviceComponent(Component):
    lc1_reset_button = MappedControl()
    lc1_encoders = control_list(MappedControl, control_count=6)

    lc2_reset_button = MappedControl()
    lc2_encoders = control_list(MappedControl, control_count=6)

    lc3_reset_button = MappedControl()
    lc3_encoders = control_list(MappedControl, control_count=6)

    lc4_reset_button = MappedControl()
    lc4_encoders = control_list(MappedControl, control_count=3)

    lc5_reset_button = MappedControl()
    lc5_encoders = control_list(MappedControl, control_count=3)

    @log_function_call()
    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(name="LeadControls", *args, **kwargs)
        self._devices: Dict[LeadControlTag, any] = {
            tag: None
            for tag
            in LeadControlTag
        }
        self._reset_parameters: Dict[LeadControlTag, any] = {
            tag: None
            for tag
            in LeadControlTag
        }

    def reset_all_devices(self):
        for tag, parameter in self._reset_parameters.items():
            if parameter is not None:
                toggle_or_cycle_parameter_value(parameter)
                toggle_or_cycle_parameter_value(parameter)

    @log_function_call()
    def set_device(self, tag: LeadControlTag, device):
        self._devices[tag] = device
        self._assign_device_to_controls(tag, device)

    def clear_all_devices(self):
        for tag in self._devices.keys():
            self.clear_device(tag)

    def clear_device(self, tag: LeadControlTag):
        self._unassign_device_controls(tag)
        self._devices[tag] = None
        self._reset_parameters[tag] = None

    def get_active_tags(self):
        return [
            tag.value
            for tag, device
            in self._devices.items()
            if device is not None
        ]

    def _unassign_device_controls(self, tag: LeadControlTag):
        encoders = self._get_encoders(tag)
        reset_button = self._get_reset_button(tag)
        reset_button.mapped_parameter = None
        for encoder in encoders:
            encoder.mapped_parameter = None

    def _assign_device_to_controls(self, tag: LeadControlTag, device):
        encoders = self._get_encoders(tag)
        reset_button = self._get_reset_button(tag)
        for encoder_count, encoder in enumerate(encoders, start=1):
            encoder_parameter = get_parameter_by_name(f"macro_dial_{encoder_count}", device)
            encoder.mapped_parameter = encoder_parameter
            LOGGER.info(f"Mapped '{tag}/{device.name}/{encoder_parameter.name}' to 'encoder/{encoder_count}'")
        reset_parameter = get_parameter_by_name("reset_button", device)
        reset_button.mapped_parameter = reset_parameter
        self._reset_parameters[tag] = reset_parameter
        LOGGER.info(f"Mapped '{tag}/{device.name}/{reset_parameter.name}' to 'button'")

    def _get_encoders(self, tag: LeadControlTag):
        return getattr(self, f"{tag.name.lower()}_encoders")

    def _get_reset_button(self, tag: LeadControlTag):
        return getattr(self, f"{tag.name.lower()}_reset_button")
