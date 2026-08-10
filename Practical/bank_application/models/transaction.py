from datetime import datetime

from enums.transaction_types import TransactionTypes
from enums.transaction_status import TransactionStatus


class Transaction:

    def __init__(
        self, 
        transaction_id: str, 
        transaction_type: TransactionTypes, 
        amount: float, 
        status: TransactionStatus = TransactionStatus.PENDING,
        source_account: str | None = None,
        destination_account: str | None = None,
        description: str | None = None
    ):
        self.transaction_id = transaction_id
        self.transaction_type = transaction_type
        self.amount = amount
        self.status = status
        self.source_account = source_account
        self.destination_account = destination_account
        self.description = description
        self.timestamp = datetime.now()

    def mark_success(self) -> None:
        self.status = TransactionStatus.SUCCESS

    def mark_failed(self) -> None:
        self.status = TransactionStatus.FAILED

    def __str__(self) -> str:
        return (
            f"{self.transaction_id} | "
            f"{self.transaction_type.value} | "
            f"{self.amount:.2f} | "
            f"{self.status.value} | "
            f"{self.timestamp:%Y-%m-%d %H:%M:%S}"
        )

    def to_dict(self) -> dict:
        return {
            "transaction_id": self.transaction_id,
            "transaction_type": self.transaction_type.value,
            "amount": self.amount,
            "status": self.status.value,
            "source_account": self.source_account,
            "destination_account": self.destination_account,
            "description": self.description,
            "timestamp": self.timestamp.isoformat()
        }

    @classmethod
    def from_dict(cls, data: dict):

        transaction = cls(
            transaction_id = data["transaction_id"],
            transaction_type = TransactionTypes(data["transaction_type"]),
            amount =float(data["amount"]),
            status = TransactionStatus(data["status"]),
            source_account = data.get("source_account"),
            destination_account = data.get("destination_account"),
            description = data.get("description"),
        )

        transaction.timestamp = datetime.fromisoformat(
            data["timestamp"]
        )

        return transaction


    