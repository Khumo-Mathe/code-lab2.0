from collections import defaultdict
from datetime import datetime


class ChatServer:
    """
    Simple real-time chat backend logic.
    """

    def __init__(self):
        self.rooms = defaultdict(list)
        self.users = set()

    def register_user(self, username):
        """
        Register a new user.
        """

        if username in self.users:
            return {
                "success": False,
                "message": "Username already exists"
            }

        self.users.add