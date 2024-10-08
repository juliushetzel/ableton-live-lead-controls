from ableton.v2.base import listens, listens_group
from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import (
    control_matrix,
    control_list,
    EncoderControl,
    MappedControl, ButtonControl
)
from ableton.v3.control_surface.elements import EncoderElement

from .logging import log_function_call, LOGGER
from .tag import LeadControlTag

component_count = 1


class DeviceComponent(Component):
    _ENCODER_COUNT = 6

    lc1_reset_button = MappedControl()
    lc1_encoders = control_list(MappedControl, control_count=_ENCODER_COUNT)

    lc2_reset_button = MappedControl()
    lc2_encoders = control_list(MappedControl, control_count=_ENCODER_COUNT)

    @log_function_call()
    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(name="LeadControls", *args, **kwargs)
        self._device = None

    @lc1_encoders.value
    def _on_encoder_value_change(self, value, encoder):
        LOGGER.info(f"on value change {value}, {encoder}")
        pass

    @lc1_reset_button.value
    def _on_reset_button(self):
        LOGGER.info("Reset Button")

    @log_function_call()
    def set_device(self, tag: LeadControlTag, device):
        self._device = device
        self._on_parameter_value_changed.replace_subjects(device.parameters)
        if tag == LeadControlTag.LC1:
            self._assign_device_to_encoders(tag, device, self.lc1_encoders, self.lc1_reset_button)
        if tag == LeadControlTag.LC2:
            self._assign_device_to_encoders(tag, device, self.lc2_encoders, self.lc2_reset_button)

    def _assign_device_to_encoders(self, tag, device, encoders, reset_button):
        for parameter in device.parameters:
            LOGGER.info(f"Param {parameter.name}")
            if parameter.name == "button_reset":
                reset_button.mapped_parameter = parameter
                LOGGER.info(f"Mapped '{tag}/{device.name}/{parameter.name}' to 'button'")
            if parameter.name.isdigit():
                dial_parameter_index = int(parameter.name)
                encoder_index = dial_parameter_index - 1
                if encoder_index < self._ENCODER_COUNT:
                    control = encoders[encoder_index]
                    control.mapped_parameter = parameter
                    LOGGER.info(f"Mapped '{tag}/{device.name}/{parameter.name}' to 'encoder/{encoder_index}'")

    @listens_group('value')
    def _on_parameter_value_changed(self, parameter):
        # LOGGER.info(f"{self} - Param changes {parameter}")
        pass
