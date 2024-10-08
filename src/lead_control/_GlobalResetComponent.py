from typing import List, Callable

from _Framework.ControlElement import ControlElement
from _Framework.CompoundComponent import CompoundComponent
from _Framework.DeviceComponent import DeviceComponent
from _Framework.SessionComponent import SessionComponent

from .logging_utils import LOGGER


class GlobalResetComponent(CompoundComponent):
    _LEAD_CONTROL_DEVICE_CONTROL_COUNT = 33

    def __init__(
            self,
            device_tags: List[str],
            reset_control: ControlElement
    ):
        CompoundComponent.__init__(self)
        self._track_index = -1
        self._scene_offset = 1
        self._controls = self._create_parameter_controls(reset_control)
        self._device_components = {
            device_tag: self.register_component(DeviceComponent())
            for device_tag
            in device_tags
        }

    def assign_device(
            self,
            tag: str,
            device: any
    ):
        component = self._device_components[tag]
        component.set_lock_to_device(True, device)
        component.set_parameter_controls(self._controls)

    def _create_parameter_controls(
            self,
            reset_control: ControlElement
    ):
        return (
            *[None for _ in range(0, self._LEAD_CONTROL_DEVICE_CONTROL_COUNT - 1)],
            reset_control
        )
