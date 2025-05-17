import re
from typing import Union

from ableton.v2.base import listens
from ableton.v3.control_surface import (
    ControlSurface, )
from ableton.v3.live import flatten_device_chain

from .device_component import DeviceComponent
from .logging import LOGGER, log_function_call
from .specification import Specification
from .tag import LeadControlTag


# TODO reload devices
# TODO Master device component

class LeadControl(ControlSurface):
    _LEAD_CONTROL_M4L_DEVICE_NAME = "Lead Control"

    @log_function_call()
    def __init__(self, c_instance):
        super().__init__(Specification, c_instance=c_instance)
        self.show_message("LeadControl Loaded")
        LOGGER.info("LeadControl loaded")

    def setup(self):
        super().setup()
        self._LeadControl__on_selected_track_changed.subject = self.song.view
        self._LeadControl__on_devices_changed.subject = self.song.view.selected_track
        self._device_component = self.component_map["LeadControls"]
        self._index_lead_controls()
        performance_component = self.component_map["PerformanceControls"]
        performance_component.set_reset_all_devices_callback(self._device_component.reset_all_devices)
        performance_component.set_index_devices_callback(self._index_lead_controls)

    @listens("selected_track")
    def __on_selected_track_changed(self):
        self._LeadControl__on_devices_changed.subject = self.song.view.selected_track

    @listens("devices")
    def __on_devices_changed(self):
        selected_track = self.song.view.selected_track
        tag = self._get_track_lead_control_tag(selected_track)
        if tag is not None:
            LOGGER.info(f"Found LC track {tag}")
            self._setup_lead_control_track(selected_track, tag)

    def disconnect(self):
        self.show_message("Disconnecting LeadControl")
        super().disconnect()

    def _index_lead_controls(self):
        for track in self.song.tracks:
            tag = self._get_track_lead_control_tag(track)
            if tag is not None:
                self._setup_lead_control_track(track, tag)
        self._show_loaded_devices_message()

    def _get_track_lead_control_tag(self, track: any) -> Union[LeadControlTag, None]:
        match = re.search(r'\[(LC)(\d+)\]', track.name)
        if isinstance(match, re.Match):
            match = match.group()
        if match is not None:
            return LeadControlTag.from_value(match)
        return None

    def _setup_lead_control_track(self, track: any, tag: LeadControlTag):
        component: DeviceComponent = self.component_map["LeadControls"]
        device = self._find_lead_control_device(track)
        if device is None:
            component.clear_device(tag)
        else:
            component.set_device(tag, device)
        self._show_loaded_devices_message()

    def _find_lead_control_device(self, track):
        for device in flatten_device_chain(track):
            if device.name == self._LEAD_CONTROL_M4L_DEVICE_NAME:
                return device

    def _show_loaded_devices_message(self):
        active_tags = ", ".join(self._device_component.get_active_tags())
        LOGGER.info(f"Loaded: {active_tags}")
        self.show_message(f"Loaded: {active_tags}")
