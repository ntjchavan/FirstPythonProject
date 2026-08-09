from models.accounts import BankAccount
from models.customer import Customer
from enums.account_types import AccountTypes
from services.bank_service import BankService
from services.transaction_service import TransactionService
from exceptions.account_exceptions import AccountNotFoundException, InsufficientBalanceException, AccountException
from audit.audit_service import AuditService
from repositories.bank_repository import BankRepository
from repositories.transaction_repository import TransactionRepository

def print_menu():
    print("\n")
    print("="*50)
    print("          Python Banking Application")
    print("="*50)

    print("1. Create Account")
    print("2. View Account")
    print("3. List All Accounts")
    print("4. Deposit Money")
    print("5. Withdraw Money")
    print("6. Transfer Money")
    print("7. Transaction History")
    print("8. Export Transactions")
    print("9. Exit")

    print("="*50)


def list_all_account(bank_service: BankService):
    print("\n---------- All Accounts ------------")
    accounts = bank_service.get_all_accounts()

    if not accounts:
        print("No account found.")
        return

    for account in accounts:
        print(account)

def view_account(bank_service: BankService):
    print("\n------------ View Account -------------")

    account_number = input("Enter account number: ").strip()

    try:
        print("\n******* Account details *******")
        account = bank_service.get_account(account_number)

        print(account)
    except AccountException as err:
        print(f"Error: {err}")

def create_account(bank_service: BankService):
    print("\n----------- Create Account ------------")

    account_number = input("Enter account number: ").strip()

    print("\nAccount Types")
    print("1. Savings")
    print("2. Current")
    account_type_choice = input("Select account type: ").strip()
    if account_type_choice == "1":
        account_type = AccountTypes.SAVINGS
    elif account_type_choice == "2":
        account_type = AccountTypes.CURRENT
    else:
        print("Invalid account type.")
        return

    try:
        initial_account_balance = float(input("Enter initial account balance: "))

        account = BankAccount(
            account_number,
            account_type,
            initial_account_balance
        )

        bank_service.add_account(account)

        print(f"Account {account_number} created successfully.")
    except ValueError as v_err:
        print("Please enter a valid amount.")

    except AccountException as a_err:
        print(f"Error: {a_err}")

def deposit_money(transaction_service: TransactionService):
    print("\n--------- Deposit Money -----------")

    account_number = input("Enter account number: ").strip()

    try:
        amount = float(input("Enter deposit amount: "))

        transaction = transaction_service.deposit(account_number, amount)

        print("\nDeposit Successfull!")
        print(transaction)
        
    except (ValueError, AccountException) as err:
        print(f"Error: {err}")


def main():
    bank_repository = BankRepository()

    transaction_repository = (
        TransactionRepository()
    )

    bank_service = BankService(
        bank_repository
    )

    audit_service = AuditService(
        transaction_repository
    )

    transaction_service = TransactionService(bank_service, audit_service)

    while True:
        print_menu()

        choice = input("Enter you choice: ").strip()

        match choice:
            case "1":
                create_account(bank_service)

            case "2":
                view_account(bank_service)

            case "3":
                list_all_account(bank_service)

            case "4":
                deposit_money(transaction_service)

            case "9":
                print("\nThank you for using Python Banking application!")
                break

            case _:
                print("Invalid choice, please choose correct choice")

if __name__ == "__main__":
    main()