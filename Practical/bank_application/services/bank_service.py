from models.accounts import BankAccount
from exceptions.account_exceptions import AccountNotFoundException

class BankService:

    def __init__(self):
        self.accounts: dict[str, BankAccount] = {}

    def add_account(self, account: BankAccount) -> None:
        self.accounts[account.account_number] = account

    def get_account(self, account_number: str) -> BankAccount:
        account = self.accounts.get(account_number)

        if account is None:
            raise AccountNotFoundException(f"Account {account_number} not found")

        return account

    def get_all_accounts(self) -> list[BankAccount]:
        return list(self.accounts.values)
    

