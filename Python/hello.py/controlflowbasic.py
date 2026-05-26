from collections import defaultdict
from datetime import datetime
import hashlib


class Blockchain:
    """
    Simplified blockchain implementation.

    Demonstrates how blocks are linked
    and verified using hashes.
    """

    def __init__(self):
        self.chain = []
        self.pending_transactions = []

        # Create genesis block
        self.create_block(
            previous_hash="0"
        )

    def generate_hash(self, block_data):
        """
        Generate SHA256 hash.
        """

        encoded_data = (
            str(block_data).encode()
        )

        return hashlib.sha256(
            encoded_data
        ).hexdigest()

    def create_transaction(
        self,
        sender,
        receiver,
        amount
    ):
        """
        Add pending transaction.
        """

        transaction = {
            "sender": sender,
            "receiver": receiver,
            "amount": amount,
            "timestamp": datetime.now()
        }

        self.pending_transactions.append(
            transaction
        )

        return transaction

    def create_block(
        self,
        previous_hash
    ):
        """
        Create a new block.
        """

        block = {
            "index": len(self.chain) + 1,
            "timestamp": datetime.now(),
            "transactions": (
                self.pending_transactions
            ),
            "previous_hash": previous_hash
        }

        block_hash = self.generate_hash(
            block
        )

        block["hash"] = block_hash

        self.chain.append(block)

        # Reset pending transactions
        self.pending_transactions = []

        return block

    def mine_block(self):
        """
        Mine pending transactions.
        """

        previous_block = self.chain[-1]

        return self.create_block(
            previous_hash=previous_block["hash"]
        )

    def validate_chain(self):
        """
        Verify blockchain integrity.
        """

        for index in range(
            1,
            len(self.chain)
        ):

            current_block = self.chain[index]

            previous_block = (
                self.chain[index - 1]
            )

            # Check hash linkage
            if (
                current_block["previous_hash"]
                != previous_block["hash"]
            ):
                return False

            # Recalculate current hash
            recalculated_hash = (
                self.generate_hash({
                    "index": current_block["index"],
                    "timestamp": (
                        current_block[
                            "timestamp"
                        ]
                    ),
                    "transactions": (
                        current_block[
                            "transactions"
                        ]
                    ),
                    "previous_hash": (
                        current_block[
                            "previous_hash"
                        ]
                    )
                })
            )

            if (
                recalculated_hash
                != current_block["hash"]
            ):
                return False

        return True


# Example usage
blockchain = Blockchain()

blockchain.create_transaction(
    sender="Khumo",
    receiver="Merchant",
    amount=150
)

blockchain.create_transaction(
    sender="Alice",
    receiver="Bob",
    amount=75
)

new_block = blockchain.mine_block()

chain_valid = blockchain.validate_chain()