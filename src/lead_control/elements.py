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

        self.add_button(41, channel=2, name="Lc1_Reset_Button", is_rgb=False, is_momentary=False)
        self.add_button(43, channel=2, name="Lc2_Reset_Button", is_rgb=False, is_momentary=True)
        self.add_button(45, channel=2, name="Lc3_Reset_Button", is_rgb=False, is_momentary=True)
        self.add_button(47, channel=2, name="Lc4_Reset_Button", is_rgb=False, is_momentary=True)
        self.add_button(48, channel=2, name="Lc5_Reset_Button", is_rgb=False, is_momentary=True)

        add_encoder_matrix(
            [
                [33, 34],
                [41, 42],
                [49, 50]
            ],
            base_name="Lc1_Encoders"
        )

        add_encoder_matrix(
            [
                [35, 36],
                [43, 44],
                [51, 52]
            ],
            base_name="Lc2_Encoders"
        )

        add_encoder_matrix(
            [
                [37, 38],
                [45, 46],
                [53, 54]
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
        self.add_button(00, channel=2, name="navigation_switch_button", is_rgb=False, is_momentary=True)

        self.add_button(49, channel=2, name="reset_all_button", is_rgb=False, is_momentary=True)
        self.add_button(50, channel=2, name="previous_scene_button", is_rgb=False, is_momentary=True)
        self.add_button(51, channel=2, name="performance_switch_button", is_rgb=False, is_momentary=True)
        self.add_button(52, channel=2, name="next_scene_button", is_rgb=False, is_momentary=True)
