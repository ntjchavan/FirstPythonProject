from exceptions.account_exceptions import AccountException
from models.accounts import BankAccount
from services.bank_service import BankService
from utils.transaction_context import TransactionContext

class TransactionService:

    def __init__(self, bank_services: BankService):
        self.bank_services = bank_services

    def transfer(
        self,
        source_account_number: str,
        destination_account_number: str,
        amount: float
    ) -> None:

        source = self.bank_services.get_account(source_account_number)

        destination = self.bank_services.get_account(destination_account_number)

        if source.account_number == destination.account_number:
            raise AccountException("Source and Destination account number cannot be same")

        with TransactionContext(source, destination):
            source.withdraw(amount)
            destination.deposit(amount)
            print("Transaction done!")

        
