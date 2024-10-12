from typing import Union
import re

from ableton.v2.base import listens
from ableton.v3.control_surface import (
    ControlSurface, Layer,
)
from ableton.v3.control_surface.components import SessionComponent, SessionRingComponent, SessionNavigationComponent, \
    SceneComponent

from .specification import Specification
from .device_component import DeviceComponent
from .logging import LOGGER, log_function_call
from .tag import LeadControlTag


class LeadControl(ControlSurface):

    @log_function_call()
    def __init__(self, c_instance):
        super().__init__(Specification, c_instance=c_instance)
        self.show_message("LeadControl Loaded")
        LOGGER.info("LeadControl loaded")

    def setup(self):
        super().setup()
        self._LeadControl__on_tracks_changed.subject = self.song
        self._LeadControl__on_selected_track_changed.subject = self.song.view
        self._LeadControl__on_devices_changed.subject = self.song.view.selected_track
        self._index_lead_controls()

    @listens("tracks")
    def __on_tracks_changed(self):
        LOGGER.info(f"Tracks changed: {[track.name for track in self.song.tracks]}")

    @listens("selected_track")
    def __on_selected_track_changed(self):
        LOGGER.info(f"Selected track changed: {self.song.view.selected_track.name}")
        self._LeadControl__on_devices_changed.subject = self.song.view.selected_track

    @listens("devices")
    def __on_devices_changed(self):
        selected_track = self.song.view.selected_track
        LOGGER.info(f"Devices changed: {[device.name for device in selected_track.devices]}")
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

    @log_function_call()
    def _get_track_lead_control_tag(self, track: any) -> Union[LeadControlTag, None]:
        match = re.search(r'^\[(LC)(\d+)\]$', track.name)
        if isinstance(match, re.Match):
            match = match.group()
        if match is not None:
            return LeadControlTag.from_value(match)
        return None

    @log_function_call()
    def _setup_lead_control_track(self, track: any, tag: LeadControlTag):
        for device in track.devices:
            if device.name == "Lead Control":
                LOGGER.info(f"Found Lead Control device for {tag}")
                component: DeviceComponent = self.component_map["LeadControls"]
                component.set_device(tag, device)
