from ableton.v3.control_surface import ControlSurfaceSpecification, create_skin
from ableton.v3.control_surface.components import SessionComponent, SessionRingComponent

from .device_component import DeviceComponent
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
            lc2_reset_button="lc2_reset_button"
        ),
        "PerformanceControls": dict(
            button_switch="switch_button",
            button_reset_all="reset_all_button"
        )
    }


class Specification(ControlSurfaceSpecification):
    elements_type = Elements
    create_mappings_function = create_mappings
    component_map = {
        "LeadControls": DeviceComponent,
        "PerformanceControls": PerformanceComponent
    }
