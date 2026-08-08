
class Customer:

    def __init__(self, customer_id: str, name: str, email: str):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def __str__(self) -> str:
        return (
            f"Customer ID: {self.customer_id}, "
            f"Name: {self.name}, "
            f"Email: {self.email}"
        )

    