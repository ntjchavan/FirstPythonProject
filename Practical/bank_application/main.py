from models.accounts import BankAccount
from models.customer import Customer
from enums.account_types import AccountTypes
from services.bank_service import BankService
from services.transaction_service import TransactionService
from exceptions.account_exceptions import AccountNotFoundException, InsufficientBalanceException, AccountException
from utils.transaction_context import TransactionContext

customer = Customer("C0001", "Netaji Chava", "netajitest@gmail.com")

account = BankAccount("ACC-001", AccountTypes.SAVINGS, 10000)

print(customer)
print(account)

print("\n------- Deposit ----------")
account.deposit(5000)
account.deposit(2500)
account.deposit(10000)
print(account)

print("\n---------- Withdraw ----------")
account.withdraw(1000)
print(account)

# try:
#     account.withdraw(30000)
#     print(account)
# except ValueError as err:
#     print(f"Error: {err}")

print("\n----------- Transaction History ---------------")

for transaction in account.transactions:
    print(transaction)

print("\n------------ After transfer using Service --------------")
account_x = BankAccount("ACC-011", AccountTypes.SAVINGS, 50000)
account_y = BankAccount("ACC-012", AccountTypes.SAVINGS, 20000)

bank_service = BankService()
bank_service.add_account(account_x)
bank_service.add_account(account_y)

transaction_service = TransactionService(bank_service)

print("\n---------- before transfer ------------")
print(bank_service.get_account("ACC-011"))
print(bank_service.get_account("ACC-012"))

transaction_service.transfer("ACC-011", "ACC-012", 10000)

print("\n---------- after transfer ------------")
print(bank_service.get_account("ACC-011"))
print(bank_service.get_account("ACC-012"))

try:
    transaction_service.transfer("ACC-012", "ACC-0098", 4000)
except AccountNotFoundException as err:
    print(err)

try:
    transaction_service.transfer("ACC-011", "ACC-012", 75000)
except InsufficientBalanceException as err:
    print(err)

try:
    transaction_service.transfer("ACC-011", "ACC-011", 75000)
except AccountException as err:
    print(err)

transaction_service.transfer("ACC-012", "ACC-011", 5000)

print(account_x)
print(account_y)


# with TransactionContext(account_x, account_y):
#     account_x.withdraw(1000)

#     raise Exception("Destination account unavailable!")

# print(account_x)
# print(account_y)
