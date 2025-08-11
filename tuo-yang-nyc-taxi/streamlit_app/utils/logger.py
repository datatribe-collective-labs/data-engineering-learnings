# log_util/logger.py

import logging
import sys
import inspect

def get_logger(name: str = None) -> logging.Logger:
    """
    Returns a logger with standard console output formatting.
    - If name is None, it uses the caller's module name
    - Shared across Airflow and Streamlit containers
    """
    if name is None:
        frame = inspect.stack()[1]
        module = inspect.getmodule(frame[0])
        name = module.__name__ if module else "nyc-taxi-app"

    logger = logging.getLogger(name)

    # Avoid duplicated handlers
    if not logger.handlers:
        logger.setLevel(logging.INFO)   # Change to DEBUG if needed

        handler = logging.StreamHandler(sys.stdout)
        handler.setLevel(logging.INFO)

        formatter = logging.Formatter(
            fmt='[%(asctime)s] [%(levelname)s] [%(name)s] [%(message)s]',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        handler.setFormatter(formatter)

        logger.addHandler(handler)
        logger.propagate = False    # Prevents double logging

    return logger

# ---------------- TEST FUNCTION ----------------
if __name__ == "__main__":
    logger = get_logger()
    
    logger.info("This is a test info message (job started)")
    logger.warning("This is a test warning message (e.g. missing column)")

    try:
        # Simulate an error (division by zero)
        result = 1 / 0
    except Exception as e:    
        logger.error("Error occured during test run: %s", str(e))
        logger.exception("Full traceback for debugging:")

    logger.info("Logging test completed.")