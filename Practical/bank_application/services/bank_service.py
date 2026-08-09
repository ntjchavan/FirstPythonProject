from models.accounts import BankAccount
from exceptions.account_exceptions import (
    AccountNotFoundException,
    AccountAlreadyExistsException
)
from repositories.bank_repository import BankRepository

class BankService:

    def __init__(
        self,
        repository: BankRepository
    ):
        self.repository = repository

        self.accounts: dict[str, BankAccount] = {}

        self.load_accounts()

    def add_account(self, account: BankAccount) -> None:
        if account.account_number in self.accounts:
            raise AccountAlreadyExistsException(
                f"Account {account.account_number} already exists"
            )

        self.accounts[account.account_number] = account

        self.save_accounts()

    def get_account(self, account_number: str) -> BankAccount:
        account = self.accounts.get(account_number)

        if account is None:
            raise AccountNotFoundException(f"Account {account_number} not found")

        return account
    
    def get_all_accounts(self) -> list[BankAccount]:
        return list(self.accounts.values())
    
    def load_accounts(self) -> None:
        accounts = self.repository.load_accounts()

        self.accounts = {
            account.account_number: account
            for account in accounts
        }

    def save_accounts(self) -> None:
        self.repository.save_accounts(self.accounts.values())

    def account_exists(self, account_number: str) -> bool:
        return account_number in self.accounts
