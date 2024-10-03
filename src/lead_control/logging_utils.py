"""
        Start logging to a local logfile (logs/abletonosc.log),
        and relay error messages via OSC.
        """
import functools
import logging
import os

LOGGER = logging.getLogger("leadcontrol")


def log_exceptions():
    def decorator(fun):
        @functools.wraps(fun)
        def decorated(*args, **kwargs):
            try:
                return fun(*args, **kwargs)
            except Exception as e:
                LOGGER.exception(e)
                raise

        return decorated

    return decorator


def setup_logging(log_level: str):
    module_path = os.path.dirname(os.path.realpath(__file__))
    log_dir = os.path.join(module_path, "logs")
    if not os.path.exists(log_dir):
        os.mkdir(log_dir, 0o755)
    log_path = os.path.join(log_dir, "leadcontrol.log")

    log_file_handler = logging.FileHandler(log_path)
    log_file_handler.setLevel(log_level.upper())
    formatter = logging.Formatter('(%(asctime)s) [%(levelname)s] %(message)s')
    log_file_handler.setFormatter(formatter)
    LOGGER.addHandler(log_file_handler)
