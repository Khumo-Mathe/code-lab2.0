from datetime import datetime, timedelta


class SessionManager:
    """
    Manage user authentication sessions.
    Similar to backend session/token systems.
    """

    def __init__(self, session_timeout_minutes=30):
        self.active_sessions = {}
        self.session_timeout = timedelta(
            minutes=session_timeout_minutes
        )

    def create_session(
        self,
        user_id,
        ip_address
    ):
        """
        Create a new user session.
        """

        session_id = (
            f"session_{user_id}_"
            f"{len(self.active_sessions) + 1}"
        )

        session_data = {
            "user_id": user_id,
            "ip_address": ip_address,
            "created_at": datetime.now(),
            "last_activity": datetime.now()
        }

        self.active_sessions[
            session_id
        ] = session_data

        return {
            "success": True,
            "session_id": session_id
        }

    def validate_session(self, session_id):
        """
        Check if session is valid and active.
        """

        if session_id not in self.active_sessions:
            return {
                "valid": False,
                "message": "Session not found"
            }

        session = self.active_sessions[
            session_id
        ]

        current_time = datetime.now()

        inactive_duration = (
            current_time
            - session["last_activity"]
        )

        # Expire inactive sessions
        if inactive_duration > self.session_timeout:

            del self.active_sessions[
                session_id
            ]

            return {
                "valid": False,
                "message": "Session expired"
            }

        # Update activity timestamp
        session["last_activity"] = current_time

        return {
            "valid": True,
            "user_id": session["user_id"]
        }

    def logout(self, session_id):
        """
        Destroy a session.
        """

        if session_id not in self.active_sessions:
            return {
                "success": False,
                "message": "Session not found"
            }

        del self.active_sessions[session_id]

        return {
            "success": True,
            "message": "Logged out successfully"
        }

    def active_user_count(self):
        """
        Return number of active sessions.
        """

        return len(self.active_sessions)


# Example usage
manager = SessionManager(
    session_timeout_minutes=15
)

session = manager.create_session(
    user_id="khumo",
    ip_address="192.168.1.10"
)

validation = manager.validate_session(
    session["session_id"]
)

active_users = manager.active_user_count()

logout_result = manager.logout(
    session["session_id"]
)