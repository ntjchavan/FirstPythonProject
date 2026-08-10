
import csv
from pathlib import Path

from models.transaction import Transaction

class TransactionRepository:

    def __init__(self, json_file_path: str = "Practical/bank_application/data/transactions.json"):
        self.json_file_path = Path(json_file_path)

        self.json_file_path.parent.mkdir(
            parents = True,
            exist_ok = True
        )

    def export_to_csv(self, transactions: list[Transaction]) -> None:

        with self.json_file_path.open(
            "w",
            newline = "",
            encoding = "utf-8"
        ) as file:

            writer = csv.writer(file)

            writer.writerow([
                "Transaction ID",
                "Type",
                "Amount",
                "Status",
                "Source Account",
                "Destination Account",
                "Description",
                "Timestamp"
            ])

            for transaction in transactions:
                writer.writerow([
                    transaction.transaction_id,
                    transaction.transaction_type,
                    transaction.amount,
                    transaction.status,
                    transaction.source_account,
                    transaction.destination_account,
                    transaction.description,
                    transaction.timestamp.isoformat()
                ])
