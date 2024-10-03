import sys

from .logging_utils import LOGGER, setup_logging

setup_logging("debug")
LOGGER.info(f"Running on python {sys.version}")

try:
    from .LeadControl import LeadControl
except Exception as e:
    LOGGER.exception(e)
    raise


def create_instance(c_instance):
    """ Creates and returns the LeadControl script """
    try:
        return LeadControl(c_instance)
    except Exception as e:
        LOGGER.exception(e)
        raise
