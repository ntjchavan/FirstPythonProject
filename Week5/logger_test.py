import logging

logging.basicConfig(
    filename="Week5/application.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

logging.debug("\nDebug message")
logging.info("Info message")
logging.warning("Warning message")
logging.error("Error message")