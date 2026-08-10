from enums.account_types import AccountTypes
from enums.transaction_types import TransactionTypes

from models.transaction import Transaction

from exceptions.account_exceptions import (
    InsufficientBalanceException,
    InvalidAccountException
)
# from exceptions.account_exceptions import InvalidAccountException

class BankAccount:

    def __init__(
        self, 
        account_number: str, 
        account_type: AccountTypes, 
        balance: float = 0.0
    ):
        self.account_number = account_number
        self.account_type = account_type
        self.balance = balance
        self.transactions: list[Transaction] = []

    def _generate_transaction_id(self) -> str:
        return f"TXN{len(self.transactions) + 1:04d}"
    
    def deposit(self, amount) -> None:
        if amount <= 0:
            raise InvalidAccountException("Deposit amount must be greater that zero.")

        # transaction = Transaction(
        #     self._generate_transaction_id(),
        #     TransactionTypes.DEPOSIT,
        #     amount
        # )
        
        self.balance += amount

        # transaction.mark_success()

        # self.transactions.append(transaction)

    def withdraw(self, amount) -> None:
        if amount <= 0:
            raise InvalidAccountException("Withdraw amount must be greater than zero.")

        if amount > self.balance:
            raise InsufficientBalanceException(f"Insufficient balance in account {self.account_number}.")

        # transaction = Transaction(
        #     self._generate_transaction_id(),
        #     TransactionTypes.WITHDRAW,
        #     amount
        # )
        
        self.balance -= amount

        # transaction.mark_success()

        # self.transactions.append(transaction)
    
    def add_transaction(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def get_balance(self) -> float:
        return self.balance

    def get_transaction(self) -> list[Transaction]:
        return self.transactions

    def __str__(self) -> str:
        return (
            f"Account Number: {self.account_number}, "
            f"Account Type: {self.account_type}, "
            f"Baance: {self.balance:.2f}"
        )

    def to_dict(self) -> dict:
        return {
            "account_number": self.account_number,
            "account_type": self.account_type.value,
            "balance": self.balance,
            "transactions":[
                transaction.to_dict()
                for transaction in self.transactions
            ]
        }

    @classmethod
    def from_dict(cls, data: dict):
        account = cls(
            account_number = data["account_number"],
            account_type = AccountTypes(data["account_type"]),
            balance =float(data["balance"])
        )

        account.transactions = [
            Transaction.from_dict(transaction)
            for transaction in data.get(
                "transactions", 
                []
            )
        ]

        return account
    