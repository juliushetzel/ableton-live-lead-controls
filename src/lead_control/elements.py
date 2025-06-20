from ableton.v3.control_surface import MIDI_NOTE_TYPE, ElementsBase, MapMode
from functools import partial

from .logging import log_function_call


class Elements(ElementsBase):

    @log_function_call()
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        add_encoder_matrix = partial(
            self.add_encoder_matrix,
            channels=1,
            is_feedback_enabled=True,
            needs_takeover=False,
        )

        add_button_matrix = partial(
            self.add_button_matrix,
            channels=2,
            is_rgb=False,
            is_momentary=True
        )

        self.add_button(1, channel=2, name="reset_encoders_button", is_rgb=False, is_momentary=True)

        self.add_button(33, channel=2, name="navigation_switch_button", is_rgb=False, is_momentary=True)
        add_button_matrix(
            [
                [34, 35 ,36 ,37, 38, 39, 40]
            ],
            base_name="fx_buttons"
        )
        add_encoder_matrix(
            [
                [2, 3, 4, 5, 6, 7, 8]
            ],
            base_name="fx_encoders"
        )

        self.add_button(41, channel=2, name="Lc1_Reset_Button", is_rgb=False, is_momentary=False)
        self.add_button(43, channel=2, name="Lc2_Reset_Button", is_rgb=False, is_momentary=True)
        self.add_button(45, channel=2, name="Lc3_Reset_Button", is_rgb=False, is_momentary=True)
        self.add_button(47, channel=2, name="Lc4_Reset_Button", is_rgb=False, is_momentary=True)
        self.add_button(48, channel=2, name="Lc5_Reset_Button", is_rgb=False, is_momentary=True)

        add_encoder_matrix(
            [
                [33, 41, 49],
                [34, 42, 50]
            ],
            base_name="Lc1_Encoders"
        )

        add_encoder_matrix(
            [
                [35, 43, 51],
                [36, 44, 52]
            ],
            base_name="Lc2_Encoders"
        )

        add_encoder_matrix(
            [
                [37, 45, 53],
                [38, 46, 54]
            ],
            base_name="Lc3_Encoders"
        )

        add_encoder_matrix(
            [
                [39],
                [47],
                [55]
            ],
            base_name="Lc4_Encoders"
        )

        add_encoder_matrix(
            [
                [40],
                [48],
                [56]
            ],
            base_name="Lc5_Encoders"
        )

        self.add_button(49, channel=2, name="reset_all_button", is_rgb=False, is_momentary=True)
        self.add_button(50, channel=2, name="previous_scene_button", is_rgb=False, is_momentary=True)
        self.add_button(51, channel=2, name="performance_switch_button", is_rgb=False, is_momentary=True)
        self.add_button(52, channel=2, name="next_scene_button", is_rgb=False, is_momentary=True)
