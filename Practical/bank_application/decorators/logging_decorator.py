from functools import wraps
from utils.logger import logger

def log_operation(func):

    @wraps(func)
    def wrapper(*args, **kwargs):
        logger.info(f"Operation started: {func.__name__}")

        try:
            result = func(*args, **kwargs)

            logger.info(f"Operation completed: {func.__name__}")

            return result
        except Exception as err:
            logger.error(f"Operation failed: {func.__name__} | {err}")

            raise

    return wrapper

# Other decorator: specific to transfer method
def log_transfer(func):

    @wraps(func)
    def wrapper(
        self,
        source_account_number,
        destination_account_number,
        amount,
        *args, 
        **kwargs
    ):
        logger.info(
            f"Transfer started | "
            f"{source_account_number} -> "
            f"{destination_account_number} | "
            f"Rs{amount:.2f}"
        )

        try:
            result = func(
                self, 
                source_account_number, 
                destination_account_number, 
                amount, 
                *args, 
                **kwargs
            )

            logger.info(
                f"Transfer Completed | "
                f"{source_account_number} -> "
                f"{destination_account_number} | "
                f"Rs{amount:.2f}"
            )

            return result
        
        except Exception as err:
            logger.error(
                f"Transfer failed | "
                f"{source_account_number} -> "
                f"{destination_account_number} | "
                f"Rs{amount:.2f}"
                f"{err}"
            )
            raise

    return wrapper

