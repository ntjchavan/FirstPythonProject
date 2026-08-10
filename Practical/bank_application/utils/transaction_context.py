from models.accounts import BankAccount

class TransactionContext:

    def __init__(self, source: BankAccount, destination: BankAccount):
        self.source = source
        self.destination = destination

        # Save balances
        self.source_balance = source.balance
        self.destination_balance = destination.balance

        # Save transaction history
        self.source_transaction = list(source.transactions)
        self.destination_transaction = list(destination.transactions)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, tracebook):
        if exc_type is None:
            print("Transaction Committed.")

        else:
            print("Transaction failed.")
            print("Rolling back transactions.")

            # Restore balances
            self.source.balance = self.source_balance
            self.destination.balance = self.destination_balance

            # Restore transaction history
            self.source.transactions = self.source_transaction
            self.destination.transactions = self.destination_transaction

        return False
    

