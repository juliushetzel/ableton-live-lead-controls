from ableton.v3.control_surface import Component
from ableton.v3.control_surface.controls import (
    control_list,
    MappedControl,
    ButtonControl
)
from ableton.v3.live import get_parameter_by_name
from ableton.v3.live.action import toggle_or_cycle_parameter_value, action

from .logging import log_function_call, LOGGER
from .utils import find_device_by_name, flatten_chains, find_devices_by_prefix, find_device_by_prefix


class EffectsComponent(Component):
    fx_buttons = control_list(MappedControl, control_count=7)
    fx_encoders = control_list(MappedControl, control_count=7)

    reset_encoders_button = ButtonControl()

    @log_function_call()
    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(name="EffectControls", *args, **kwargs)
        self._reset_params: dict = {}

    @reset_encoders_button.pressed
    def _reset_all_controls(self, _):
        self._set_mapped_controls_state(self.fx_encoders, False)
        self._set_mapped_controls_state(self.fx_buttons, True)

    def _set_mapped_controls_state(self, controls, enabled):
        for control in controls:
            if control.mapped_parameter is None:
                continue
            value = control.mapped_parameter.max if enabled else control.mapped_parameter.min
            control.mapped_parameter.value = value

    def reset_toggle_buttons(self):
        self._set_mapped_controls_state(self.fx_buttons, False)

    def set_fx_tracks(
            self,
            tracks: list
    ):
        self._unassign_controls()
        control_index = 0
        for track_index, track in enumerate(tracks):
            fx_devices_chain = find_device_by_prefix(track.devices, "FX CHAIN")
            if fx_devices_chain is None:
                return

            all_devices = flatten_chains(fx_devices_chain.chains)
            fx_devices = find_devices_by_prefix(all_devices, "LiveFX ")

            for device in fx_devices:
                if control_index >= 7:
                    LOGGER.info(f"Only 7 controls allowed")
                    return
                self._assign_controls(control_index, device)
                control_index = control_index + 1


    def _assign_controls(self, control_index, device):
        encoder = self.fx_encoders[control_index]
        button = self.fx_buttons[control_index]

        parameters = self._find_parameters(device)
        device, toggle, mix = parameters
        button.mapped_parameter = toggle
        LOGGER.info(f"Mapped '{device.name}/{toggle.name}' to 'button/{control_index}'")
        encoder.mapped_parameter = mix
        LOGGER.info(f"Mapped '{device.name}/{mix.name}' to 'encoder/{control_index}'")


    def _find_parameters(self, device) -> tuple:
        on_off_toggle = None
        mix_poti = None
        for parameter in device.parameters:
            if parameter.name == "ON/OFF":
                on_off_toggle = parameter
            if parameter.name == "MIX":
                mix_poti = parameter
        if None in (on_off_toggle, mix_poti):
            raise Exception(f"Could not find 'ON/OFF' or 'MIX' parameter for '{device.name}'")
        return (device, on_off_toggle, mix_poti)

    def _find_all_fx_devices(self, devices) -> list:
        devices = find_devices_by_prefix(devices, "LiveFX ")
        return devices

    def _unassign_controls(self):
        for control in [
            *self.fx_buttons,
            *self.fx_encoders
        ]:
            control.mapped_parameter = None
