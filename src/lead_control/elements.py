from ableton.v3.control_surface import MIDI_NOTE_TYPE, ElementsBase, MapMode
from functools import partial

from .logging import log_function_call


class Elements(ElementsBase):

    @log_function_call()
    def __init__(self, *a, **k):
        super().__init__(*a, **k)
        add_button_matrix = partial(
            self.add_button_matrix,
            msg_type=MIDI_NOTE_TYPE,
            led_channel=2,
            is_rgb=False,
            is_momentary=False,
        )
        add_encoder_matrix = partial(
            self.add_encoder_matrix,
            channels=1,
            is_feedback_enabled=True,
            needs_takeover=False,
            # map_mode=MapMode.LinearBinaryOffset
        )

        # Report values?
        self.add_element()

        self.add_button(41, channel=2, name="Lc1_Reset_Button", is_rgb=False, is_momentary=False)
        self.add_button(43, channel=2, name="Lc2_Reset_Button", is_rgb=False, is_momentary=True)

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
        #
        # add_button_matrix(
        #     [list(range(9, 16 + 1))],
        #     base_name="Master_buttons"
        # )
        #
        # add_button_matrix(
        #     [list(range(17, 24 + 1))],
        #     base_name="LC_Buttons"
        # )
        #
        # add_encoder_matrix(
        #     [list(range(33, 56 + 1))],
        #     base_name="Device_Controls"
        # )
        #
        # add_button_matrix(
        #     [list(range(49, 52 + 1))],
        #     base_name="Session_Buttons"
        # )
