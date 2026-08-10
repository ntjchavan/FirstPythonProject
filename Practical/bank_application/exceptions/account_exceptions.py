
class AccountException(Exception):
    """Base exception for account-related errors."""

class InsufficientBalanceException(Exception):
    """Raised when an account has insufficient balance."""

class InvalidAccountException(Exception):
    """Raised when transaction amount is invalid."""

class AccountNotFoundException(Exception):
    """Raised when an account cannot be found"""

class AccountAlreadyExistsException(Exception):
    """Raised when as account already exists"""
    