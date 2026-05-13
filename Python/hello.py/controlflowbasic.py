from collections import defaultdict


class TransactionMonitor:
    """
    Detect suspicious financial transactions
    based on configurable rules.
    """

    def __init__(self, transaction_limit):
        self.transaction_limit = transaction_limit
        self.user_totals = defaultdict(float)

    def process_transactions(self, transactions):
        """
        Analyze transactions and flag suspicious activity.

        Args:
            transactions (list): List of transaction dictionaries

        Returns:
            dict: Summary report
        """

        flagged_transactions = []
        processed_transactions = []

        for transaction in transactions:
            user_id = transaction["user_id"]
            amount = transaction["amount"]
            location = transaction["location"]

            self.user_totals[user_id] += amount

            suspicious_reasons = []

            # Rule 1: Large single transaction
            if amount > self.transaction_limit:
                suspicious_reasons.append(
                    "Large transaction amount"
                )

            # Rule 2: Rapid spending threshold
            if self.user_totals[user_id] > (
                self.transaction_limit * 3
            ):
                suspicious_reasons.append(
                    "High cumulative spending"
                )

            result = {
                "user_id": user_id,
                "amount": amount,
                "location": location,
                "suspicious": bool(suspicious_reasons),
                "reasons": suspicious_reasons
            }

            processed_transactions.append(result)

            if suspicious_reasons:
                flagged_transactions.append(result)

        return {
            "flagged_transactions": flagged_transactions,
            "processed_transactions": processed_transactions
        }


# Example transactions
transactions = [
    {
        "user_id": "U100",
        "amount": 2500,
        "location": "Johannesburg"
    },
    {
        "user_id": "U100",
        "amount": 4000,
        "location": "Cape Town"
    },
    {
        "user_id": "U100",
        "amount": 7000,
        "location": "Durban"
    }
]

monitor = TransactionMonitor(
    transaction_limit=5000
)

report = monitor.process_transactions(transactions)