from models.transaction import Transaction
from enums.transaction_status import TransactionStatus
from repositories.transaction_repository import TransactionRepository

class AuditService:

    def __init__(self, repository: TransactionRepository):
        self.repository = repository
        self.transactions: list[Transaction] = []

    def record(self, transaction: Transaction) -> None:
        self.transactions.append(transaction)

    def get_all(self) -> list[Transaction]:
        return list(self.transactions)

    def find_by_account(
        self,
        account_number: str
    ) -> list[Transaction]:
        
        return [
            transaction 
            for transaction in self.transactions
            if (
                transaction.source_account == account_number 
                or 
                transaction.destination_account == account_number
            )
        ]

    def get_successfull_transfer(
        self
    ) -> list[Transaction]:
        
        # return list(
        #     filter(
        #         lambda transaction: 
        #             transaction.status == TransactionStatus.SUCCESS, 
        #         self.transactions
        #     )
        # )
        return [
            transaction 
            for transaction in self.transactions 
            if transaction.status == TransactionStatus.SUCCESS
        ]

    def export_to_csv(self) -> None:
        self.repository.export_to_csv(self.transactions)

    def stream_transaction(self):

        for transaction in self.transactions:
            yield transaction
            
