from ableton.v3.control_surface import ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.components import SessionComponent, SessionRingComponent

from .device_component import DeviceComponent
from .effects_component import EffectsComponent
from .elements import Elements
from .logging import log_function_call
from .performance_component import PerformanceComponent


@log_function_call()
def create_mappings(control_surface):
    return {
        "LeadControls": dict(
            lc1_encoders="lc1_encoders",
            lc1_reset_button="lc1_reset_button",
            lc2_encoders="lc2_encoders",
            lc2_reset_button="lc2_reset_button",
            lc3_encoders="lc3_encoders",
            lc3_reset_button="lc3_reset_button",
            lc4_encoders="lc4_encoders",
            lc4_reset_button="lc4_reset_button",
            lc5_encoders="lc5_encoders",
            lc5_reset_button="lc5_reset_button"
        ),
        "PerformanceControls": dict(
            button_navigation_switch="navigation_switch_button",
            button_performance_switch="performance_switch_button",
            button_reset_all="reset_all_button"
        ),
        "EffectControls": dict(
            fx_buttons="fx_buttons",
            fx_encoders="fx_encoders",
            reset_encoders_button="reset_encoders_button"
        )
    }


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    create_mappings_function = create_mappings
    component_map = {
        "LeadControls": DeviceComponent,
        "PerformanceControls": PerformanceComponent,
        "EffectControls": EffectsComponent
    }
