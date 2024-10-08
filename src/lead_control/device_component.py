from typing import List, Dict

from ableton.v2.base import listens_group
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import (
    control_list,
    MappedControl
)

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
        self._devices: Dict[LeadControlTag, any] = {}

    @log_function_call()
    def set_device(self, tag: LeadControlTag, device):
        self._devices[tag] = device
        all_parameters = self._all_parameters()
        self._on_parameter_value_changed.replace_subjects(all_parameters)
        self._assign_device_to_controls(tag, device)

    def _all_parameters(self) -> List[any]:
        return [
            parameter
            for device
            in list(self._devices.values())
            for parameter
            in device.parameters
        ]

    def _assign_device_to_controls(self, tag: LeadControlTag, device):
        encoders = self._get_encoders(tag)
        reset_button = self._get_reset_button(tag)
        for parameter in device.parameters:
            LOGGER.info(f"Param {parameter.name}")
            if parameter.name == "button_reset":
                reset_button.mapped_parameter = parameter
                LOGGER.info(f"Mapped '{tag}/{device.name}/{parameter.name}' to 'button'")
            if parameter.name.isdigit():
                dial_parameter_index = int(parameter.name)
                encoder_index = dial_parameter_index - 1
                if encoder_index < encoders.control_count:
                    control = encoders[encoder_index]
                    control.mapped_parameter = parameter
                    LOGGER.info(f"Mapped '{tag}/{device.name}/{parameter.name}' to 'encoder/{encoder_index}'")

    def _get_encoders(self, tag: LeadControlTag):
        return getattr(self, f"{tag.name.lower()}_encoders")

    def _get_reset_button(self, tag: LeadControlTag):
        return getattr(self, f"{tag.name.lower()}_reset_button")

    @listens_group('value')
    def _on_parameter_value_changed(self, parameter):
        # LOGGER.info(f"{self} - Param changes {parameter}")
        pass
