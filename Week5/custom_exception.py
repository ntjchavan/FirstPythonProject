
class InsufficientBalanceException(Exception):
    pass

class InvalidAmountError(Exception):
    pass


balance = 5000
withdraw = -5500

try:

    if withdraw <= 0:
        raise InvalidAmountError(f"Withdraw amount {withdraw} should be greater than zero.")

    if withdraw > balance:
        raise InsufficientBalanceException(f"Withdraw amount {withdraw} should not be greater than balance amount {balance}")

except InsufficientBalanceException as err:
    print(f"Error: {err}")

except InvalidAmountError as err:
    print(f"Invalid amount: {err}")
    

