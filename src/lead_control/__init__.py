import sys

from .logging import LOGGER, setup_logging

setup_logging("debug")
LOGGER.info(f"Running on python {sys.version}")

try:
    from .specification import Specification
    from .lead_control import LeadControl
except Exception as e:
    LOGGER.exception(e)
    raise


def create_instance(c_instance):
    """ Creates and returns the LeadControl script """
    try:
        return LeadControl(c_instance=c_instance)
    except Exception as e:
        LOGGER.exception(e)
        raise
