from threading import Thread
from typing import Callable

from ableton.v2.base import listens
from ableton.v3.control_surface import Component, Layer
from ableton.v3.control_surface.components import SessionComponent, SessionRingComponent, SessionNavigationComponent
from ableton.v3.control_surface.controls import ButtonControl
from ableton.v3.live import action


class PerformanceComponent(Component):
    button_switch = ButtonControl()
    button_reset_all = ButtonControl()

    def __init__(
            self,
            *args,
            **kwargs
    ):
        super().__init__(name="PerformanceControls", *args, **kwargs)
        self._reset_all_devices_callback: Callable[[], None] = lambda: None
        self._switch_enabled: bool = False
        self._reset_all_on_next_scene_launch: bool = False
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

    def set_reset_all_devices_callback(self, callback: Callable[[], None]):
        self._reset_all_devices_callback = callback

    @button_switch.pressed
    def _on_switch_pressed(self, _):
        self._switch_enabled = True

    @button_switch.released
    def _on_switch_released(self, _):
        self._switch_enabled = False

    @button_reset_all.pressed
    def _on_reset_all_pressed(self, _):
        self._reset_all_devices_callback()

    @listens("offset")
    def __on_session_ring_offset_changed(self, _: int, vertical_offset: int):
        scene = self.song.scenes[vertical_offset]
        self._session.selected_scene().set_scene(scene)
        if self._switch_enabled:
            self._PerformanceComponent__on_scene_triggered_changed.subject = scene
            self._reset_all_on_next_scene_launch = True
        else:
            self._PerformanceComponent__on_scene_triggered_changed.subject = None
        action.fire(scene, button_state=True)

    @listens("is_triggered")
    def __on_scene_triggered_changed(self):
        is_triggered = self._session.selected_scene().scene.is_triggered
        if is_triggered:
            return

        reset_all_on_next_scene_launch = self._reset_all_on_next_scene_launch
        self._reset_all_on_next_scene_launch = False

        if reset_all_on_next_scene_launch:
            Thread(target=self._reset_all_devices_callback).start()
