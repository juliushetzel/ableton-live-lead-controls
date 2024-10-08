from typing import Callable

from _Framework.CompoundComponent import CompoundComponent
from _Framework.ControlElement import ControlElement
from _Framework.SessionComponent import SessionComponent


class LeadControlSessionComponent(CompoundComponent):

    def __init__(
            self,
            launch_next_scene_button: ControlElement,
            session_highlight_callback: Callable[[int, int, int, int, bool], None]
    ):
        CompoundComponent.__init__(self)
        self._track_index = -1
        self._scene_offset = 1
        self._session_component = self._create_session_component(
            launch_next_scene_button,
            session_highlight_callback,
        )
        self.register_component(self._session_component)

    def _create_session_component(
            self,
            launch_next_scene_button: ControlElement,
            session_highlight_callback: Callable[[int, int, int, int, bool], None]
    ) -> SessionComponent:
        session_component = SessionComponent(
            num_tracks=100,
            num_scenes=1,
            auto_name=True,
        )
        session_component.set_select_next_button(launch_next_scene_button)
        session_component.set_show_highlight(True)
        session_component.set_highlighting_callback(session_highlight_callback)
        return session_component
