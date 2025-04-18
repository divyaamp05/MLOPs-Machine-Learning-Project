from US_VISA.logger import get_logger
from US_VISA.exception import USvisaException

logger = get_logger(__name__)
logger.info("This is a test log message.")

try:
    result = 10 / 0
    print("Result:", result)

except ZeroDivisionError:
    print("Error: Cannot divide by zero!")

finally:
    print("Done.")


