from typing import List, Callable

from _Framework.ControlElement import ControlElement
from _Framework.CompoundComponent import CompoundComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.SessionComponent import SessionComponent

from .logging_utils import LOGGER


class LeadControlDeviceComponent(CompoundComponent):
    _LEAD_CONTROL_DEVICE_CONTROL_COUNT = 33
    _MAX_POTIS = 8

    def __init__(
            self,
            tag: str,
            poti_controls: List[ControlElement],
            reset_control: ControlElement,
    ):
        CompoundComponent.__init__(self)
        self._track_index = -1
        self._scene_offset = 1
        self._tag = tag
        self._controls = self._create_parameter_controls(poti_controls, reset_control)
        self._device_component = DeviceComponent()
        self.register_component(self._device_component)

    def assign_device(self, device: any):
        LOGGER.info(f"assigning device {device.name} to {self._tag}")
        self._device_component.set_lock_to_device(lock=True, device=device)
        self._device_component.set_parameter_controls(self._controls)

    def _create_parameter_controls(
            self,
            poti_controls: List[ControlElement],
            reset_control: ControlElement
    ):
        assert len(poti_controls) <= self._MAX_POTIS

        poti_count = len(poti_controls)
        parameter_controls = []
        for poti in poti_controls:
            parameter_controls.append(poti)
        for _ in range(0, self._LEAD_CONTROL_DEVICE_CONTROL_COUNT - poti_count - 1):
            parameter_controls.append(None)
        parameter_controls.append(reset_control)
        return parameter_controls
