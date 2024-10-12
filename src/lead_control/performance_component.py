from ableton.v2.base import listens

from ableton.v3.control_surface import Component, Layer
from ableton.v3.control_surface.components import SessionComponent, SessionRingComponent, SessionNavigationComponent
from ableton.v3.control_surface.controls import ButtonControl

from .logging import LOGGER


class PerformanceComponent(Component):
    button_switch = ButtonControl()
    button_reset_all = ButtonControl()

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(name="PerformanceControls", *args, **kwargs)
        self._switch_enabled = False
        self._session_ring = SessionRingComponent(
            name='Session_Ring',
            is_enabled=True,
            num_tracks=40,
            num_scenes=1
        )
        self._session = SessionComponent(
            name='Session',
            session_ring=self._session_ring
        )
        self._session_navigation = SessionNavigationComponent(
            name='Session_Navigation',
            is_enabled=False,
            session_ring=self._session_ring,
            layer=Layer(
                up_button="previous_scene_button",
                down_button="next_scene_button"
            )
        )
        self._session_navigation.set_enabled(True)
        self._PerformanceComponent__on_session_ring_offset_changed.subject = self._session_ring

    @button_switch.pressed
    def _on_switch_pressed(self, _):
        LOGGER.info("Switch pressed")
        self._switch_enabled = True

    @button_switch.released
    def _on_switch_released(self, _):
        LOGGER.info("Switch released")
        self._switch_enabled = False

    @button_reset_all.pressed
    def _on_reset_all_pressed(self, _):
        pass
        # if self._switch_enabled:
        #     pass
        # else:
        #     self._session.selected_scene()._on_launch_button_pressed()

    @listens("offset")
    def __on_session_ring_offset_changed(self, _: int, vertical_offset: int):
        switch_was_enabled = self._switch_enabled
        scene = self.song.scenes[vertical_offset]
        LOGGER.info(f"Selected session changed. switchenabled={self._switch_enabled}")
        self._session.selected_scene().set_scene(scene)
        if switch_was_enabled:
            self._session.selected_scene()._on_launch_button_pressed()
