from collections import defaultdict
from datetime import datetime


class NotificationSystem:
    """
    Event-driven notification service.

    Sends notifications through multiple channels.
    """

    def __init__(self):
        self.notifications = []
        self.user_preferences = defaultdict(
            lambda: {
                "email": True,
                "sms": False,
                "push": True
            }
        )

    def update_preferences(
        self,
        user_id,
        email=None,
        sms=None,
        push=None
    ):
        """
        Update notification preferences.
        """

        preferences = self.user_preferences[user_id]

        if email is not None:
            preferences["email"] = email

        if sms is not None:
            preferences["sms"] = sms

        if push is not None:
            preferences["push"] = push

        return preferences

    def send_notification(
        self,
        user_id,
        message,
        notification_type
    ):
        """
        Send notifications using enabled channels.
        """

        preferences = self.user_preferences[
            user_id
        ]

        delivery_results = []

        for channel, enabled in preferences.items():

            if not enabled:
                continue

            delivery_results.append({
                "channel": channel,
                "status": "SENT"
            })

        notification_record = {
            "user_id": user_id,
            "message": message,
            "type": notification_type,
            "timestamp": datetime.now(),
            "deliveries": delivery_results
        }

        self.notifications.append(
            notification_record
        )

        return notification_record

    def notification_history(
        self,
        user_id
    ):
        """
        Return all notifications for a user.
        """

        return [
            notification
            for notification in self.notifications
            if notification["user_id"] == user_id
        ]

    def analytics(self):
        """
        Generate notification statistics.
        """

        total_notifications = len(
            self.notifications
        )

        channel_usage = defaultdict(int)

        for notification in self.notifications:

            for delivery in notification[
                "deliveries"
            ]:

                channel_usage[
                    delivery["channel"]
                ] += 1

        return {
            "total_notifications": (
                total_notifications
            ),
            "channel_usage": dict(
                channel_usage
            )
        }


# Example usage
system = NotificationSystem()

system.update_preferences(
    user_id="khumo",
    sms=True
)

notification = system.send_notification(
    user_id="khumo",
    message="Your report is ready",
    notification_type="REPORT"
)

history = system.notification_history(
    user_id="khumo"
)

analytics = system.analytics()