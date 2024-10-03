from _Framework.ButtonElement import ButtonElement
from _Framework.InputControlElement import MIDI_CC_TYPE
from _Framework.SliderElement import SliderElement

SLIDER_CHANNEL = 2
BUTTON_CHANNEL = 3


class BcrControlsMap:

    def __init__(self):
        self._control_map = (
            # Top row 0-7
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 1),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 2),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 3),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 4),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 5),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 6),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 7),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 8),

            # Encoder Buttons 8-15
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 1),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 2),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 3),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 4),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 5),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 6),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 7),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 8),

            # First Button row 16-23
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 33),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 34),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 35),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 36),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 37),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 38),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 39),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 40),

            # Second Button row 24-31
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 41),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 42),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 43),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 44),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 45),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 46),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 47),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 48),

            # First Poti row 32-39
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 33),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 34),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 35),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 36),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 37),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 38),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 39),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 40),

            # Second Poti row 40-47
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 41),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 42),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 43),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 44),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 45),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 46),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 47),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 48),

            # Third Poti row 48-55
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 49),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 50),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 51),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 52),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 53),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 54),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 55),
            SliderElement(MIDI_CC_TYPE, SLIDER_CHANNEL, 56),

            # Side Panel Buttons 56-59
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 49),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 50),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 51),
            ButtonElement(True, MIDI_CC_TYPE, BUTTON_CHANNEL, 52),
        )

    def get_device_1_potis(self):
        return (
            self._control_map[32],
            self._control_map[40],
            self._control_map[48],
            self._control_map[33],
            self._control_map[41],
            self._control_map[49],
        )

    def get_device_1_reset(self):
        return self._control_map[24]

    def get_next_scene_button(self):
        return self._control_map[59]

    def get_reset_all_button(self):
        return self._control_map[59]

#
# BCR_DEVICE_1_RESET_CONTROL = (
#     BCR_CONTROLS[24]
# )
#
# BCR_DEVICE_2_POTI_CONTROLS = (
#     BCR_CONTROLS[34],
#     BCR_CONTROLS[42],
#     BCR_CONTROLS[50],
#     BCR_CONTROLS[35],
#     BCR_CONTROLS[43],
#     BCR_CONTROLS[51],
# )
# BCR_DEVICE_2_RESET_CONTROL = (
#     BCR_CONTROLS[26]
# )

[print("Hallo") for _ in range(1, 4)]
