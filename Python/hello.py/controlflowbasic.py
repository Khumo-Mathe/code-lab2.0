from collections import defaultdict
from datetime import datetime
import uuid


class PaymentProcessor:
    """
    Simulates a digital payment processing system.
    """

    def __init__(self):
        self.accounts = defaultdict(float)
        self.transactions = []

    def create_account(
        self,
        user_id,
        initial_balance=0
    ):
        """
        Create a user wallet/account.
        """

        self.accounts[user_id] = initial_balance

        return {
            "user_id": user_id,
            "balance": initial_balance
        }

    def transfer(
        self,
        sender,
        receiver,
        amount
    ):
        """
        Transfer money between accounts.
        """

        if sender not in self.accounts:
            return {
                "success": False,
                "message": "Sender not found"
            }

        if receiver not in self.accounts:
            return {
                "success": False,
                "message": "Receiver not found"
            }

        if amount <= 0:
            return {
                "success": False,
                "message": "Invalid amount"
            }

        if self.accounts[sender] < amount:
            return {
                "success": False,
                "message": "Insufficient funds"
            }

        # Debit sender
        self.accounts[sender] -= amount

        # Credit receiver
        self.accounts[receiver] += amount

        transaction = {
            "transaction_id": str(uuid.uuid4()),
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": datetime.now(),
            "status": "SUCCESS"
        }

        self.transactions.append(transaction)

        return {
            "success": True,
            "transaction": transaction
        }

    def account_balance(self, user_id):
        """
        Return account balance.
        """

        if user_id not in self.accounts:
            return None

        return {
            "user_id": user_id,
            "balance": round(
                self.accounts[user_id],
                2
            )
        }

    def transaction_history(
        self,
        user_id
    ):
        """
        Return user transaction history.
        """

        return [
            transaction
            for transaction in self.transactions
            if (
                transaction["sender"] == user_id
                or transaction["receiver"] == user_id
            )
        ]


# Example usage
processor = PaymentProcessor()

processor.create_account(
    user_id="khumo",
    initial_balance=5000
)

processor.create_account(
    user_id="merchant_1",
    initial_balance=1000
)

payment = processor.transfer(
    sender="khumo",
    receiver="merchant_1",
    amount=750
)

balance = processor.account_balance(
    "khumo"
)

history = processor.transaction_history(
    "khumo"
)