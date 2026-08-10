from exceptions.account_exceptions import AccountException
from services.bank_service import BankService
from utils.transaction_context import TransactionContext
from decorators.logging_decorator import log_transfer
from audit.audit_service import AuditService
from models.transaction import Transaction
from enums.transaction_types import TransactionTypes
from enums.transaction_status import TransactionStatus

class TransactionService:

    def __init__(self, bank_services: BankService, audit_service: AuditService):
        self.bank_services = bank_services
        self.audit_service = audit_service

        self.transaction_counter = (
            self._get_next_transaction_number()
        )

    def deposit(self, account_number: str, amount: float) -> Transaction:
        account = self.bank_services.get_account(account_number)
        account.deposit(amount)

        transaction = Transaction(
            transaction_id= self._generate_transaction_id(),
            transaction_type= TransactionTypes.DEPOSIT,
            amount= amount,
            status= TransactionStatus.SUCCESS,
            source_account= account_number,
            description="Cash Deposit"
        )

        transaction.mark_success()
        account.add_transaction(transaction)
        self.audit_service.record(transaction)
        self.bank_services.save_accounts()

        return transaction

    def _generate_transaction_id(self) -> str:
        # return f"TXN{len(self.transactions) + 1:04d}"
        transaction_id = (
            f"TXN{self.transaction_counter:04d}"
        )

        self.transaction_counter += 1

        return transaction_id

    def withdraw(self, account_number: str, amount: float) -> Transaction:
        account = self.bank_services.get_account(account_number)
        account.withdraw(amount)

        transaction = Transaction(
            transaction_id = self._generate_transaction_id(),
            transaction_type=TransactionTypes.WITHDRAW,
            amount= amount,
            status=TransactionStatus.SUCCESS,
            source_account=account_number,
            description="Cash withdraw"
        )

        transaction.mark_success()
        account.add_transaction(transaction)
        self.audit_service.record(transaction)

        self.bank_services.save_accounts()

        return transaction

    @log_transfer
    def transfer(
        self,
        source_account_number: str,
        destination_account_number: str,
        amount: float
    ) -> Transaction:

        source = self.bank_services.get_account(source_account_number)

        destination = self.bank_services.get_account(destination_account_number)

        if source.account_number == destination.account_number:
            raise AccountException("Source and Destination account number cannot be same")

        transaction = Transaction(
            self._generate_transaction_id(),
            TransactionTypes.TRANSFER,
            amount,
            TransactionStatus.SUCCESS,
            source_account_number,
            destination_account_number,
            "Account fransfer"
        )

        with TransactionContext(source, destination):
            source.withdraw(amount)
            destination.deposit(amount)

            transaction.mark_success()

            source.add_transaction(transaction)
            destination.add_transaction(transaction)

            self.audit_service.record(transaction)

            self.bank_services.save_accounts()

        return transaction

    def get_account_transaction(self, account_number: str) -> list[Transaction]:

        account = self.bank_services.get_account(account_number)

        return account.transactions

    def _get_next_transaction_number(self) -> int:

        transactions = self.audit_service.get_all()
        if not transactions:
            return 1

        numbers = []

        for transaction in transactions:
            try:
                number = int(
                    transaction.transaction_id.replace(
                        "TXN",
                        ""
                    )
                )
                numbers.append(number)
            except ValueError:
                continue
        if not numbers:
            return 1

        return max(numbers) + 1
