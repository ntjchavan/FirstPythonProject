import json
from pathlib import Path
import csv

from models.accounts import BankAccount

class BankRepository:

    def __init__(self, file_path: str = "Practical/bank_application/data/accounts.json"):
        self.file_path = Path(file_path)

        self.file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

    def save_accounts(
        self, 
        accounts: list[BankAccount]
    ) -> None:

        data = [
            account.to_dict()
            for account in accounts
        ]
        # print("bank repo data: ", data)

        try:
            with self.file_path.open(
                "w",
                encoding="utf-8"
            ) as file:
                
                json.dump(data, file, indent=4)
        except OSError as err:
            raise OSError(
                f"Unable to save account data: {err}"
            ) from err

    def load_accounts(self) -> list[dict]:
        if not self.file_path.exists():
            return []

        with self.file_path.open(
            "r",
            encoding="utf-8"
        ) as file:
            data = json.load(file)

        return [
            BankAccount.from_dict(account)
            for account in data
        ]

    


                