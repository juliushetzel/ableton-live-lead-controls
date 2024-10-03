import re
from typing import Union

from _Framework.ControlSurface import ControlSurface

from .GlobalResetComponent import GlobalResetComponent
from .LeadControlSessionComponent import LeadControlSessionComponent
from .logging_utils import LOGGER, log_exceptions
from .MidiMap import BcrControlsMap
from .LeadControlDeviceComponent import LeadControlDeviceComponent


class LeadControl(ControlSurface):
    def __init__(self, c_instance):
        ControlSurface.__init__(self, c_instance)
        with self.component_guard():
            all_controls = BcrControlsMap()
            self._device_components = {
                "[LC1]": LeadControlDeviceComponent(
                    "LC1",
                    all_controls.get_device_1_potis(),
                    all_controls.get_device_1_reset(),
                ),
                "[LC2]": LeadControlDeviceComponent(
                    "LC2",
                    all_controls.get_device_1_potis(),
                    all_controls.get_device_1_reset(),
                )
            }
            self._global_reset_component = GlobalResetComponent(
                list(self._device_components.keys()),
                all_controls.get_reset_all_button()
            )
            self._session_component = LeadControlSessionComponent(
                all_controls.get_next_scene_button(),
                self._set_session_highlight
            )

        LOGGER.info("LeadControl loaded")
        self.show_message("LeadControl Loaded")

    def _set_session_highlight(self, track_offset, scene_offset, width, height, include_return_tracks):
        if list((track_offset, scene_offset, width, height)).count(-1) != 4:
            pass
        self._c_instance.set_session_highlight(track_offset, scene_offset, width, height, include_return_tracks)

    @log_exceptions()
    def _on_track_list_changed(self):
        LOGGER.info("track list changed")
        self._load_devices()
        super()._on_track_list_changed()

    def _load_devices(self):
        tracks = list(self.song().tracks)
        for track_index, track in enumerate(tracks):
            tag = self._get_track_lead_control_tag(track)
            if tag is not None:
                LOGGER.info(f"Found LC track {tag}")
                self._setup_lead_control_track(track, tag, track_index)

    def _get_track_lead_control_tag(self, track: any) -> Union[str, None]:
        match = re.search(r'^\[(LC)(\d+)\]$', track.name)
        if isinstance(match, re.Match):
            match = match.group()
        return match

    def _setup_lead_control_track(self, track: any, tag: str, track_index: int):
        component = self._device_components.get(tag)
        LOGGER.info(f"Component {component}, {track_index}")
        if component is None:
            return

        for device in track.devices:
            if device.name == "Lead Control":
                LOGGER.info(f"Found Lead Control device for {tag}, track {track_index}")
                component.assign_device(device)
                self._global_reset_component.assign_device(tag, device)

    def disconnect(self):
        self.show_message("Disconnecting LeadControl")
        super().disconnect()
