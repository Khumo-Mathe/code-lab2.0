from collections import defaultdict
from datetime import datetime


class LogAnalyzer:
    """
    Analyze application/server logs
    and detect unusual activity.
    """

    def __init__(self):
        self.logs = []
        self.error_counts = defaultdict(int)
        self.ip_activity = defaultdict(int)

    def add_log(
        self,
        level,
        message,
        ip_address
    ):
        """
        Store a log entry.
        """

        log_entry = {
            "level": level,
            "message": message,
            "ip_address": ip_address,
            "timestamp": datetime.now()
        }

        self.logs.append(log_entry)

        # Track error frequency
        if level == "ERROR":
            self.error_counts[ip_address] += 1

        # Track IP activity
        self.ip_activity[ip_address] += 1

    def detect_suspicious_ips(
        self,
        error_threshold=5,
        activity_threshold=20
    ):
        """
        Detect suspicious behavior based on
        errors or excessive requests.
        """

        suspicious_ips = []

        for ip in self.ip_activity:

            if (
                self.error_counts[ip]
                >= error_threshold
            ):
                suspicious_ips.append({
                    "ip_address": ip,
                    "reason": "High error rate"
                })

            elif (
                self.ip_activity[ip]
                >= activity_threshold
            ):
                suspicious_ips.append({
                    "ip_address": ip,
                    "reason": "Excessive activity"
                })

        return suspicious_ips

    def generate_report(self):
        """
        Generate system log statistics.
        """

        total_logs = len(self.logs)

        error_logs = sum(
            1
            for log in self.logs
            if log["level"] == "ERROR"
        )

        warning_logs = sum(
            1
            for log in self.logs
            if log["level"] == "WARNING"
        )

        info_logs = sum(
            1
            for log in self.logs
            if log["level"] == "INFO"
        )

        return {
            "total_logs": total_logs,
            "error_logs": error_logs,
            "warning_logs": warning_logs,
            "info_logs": info_logs,
            "suspicious_ips": (
                self.detect_suspicious_ips()
            )
        }


# Example usage
analyzer = LogAnalyzer()

analyzer.add_log(
    level="INFO",
    message="User logged in",
    ip_address="192.168.1.10"
)

analyzer.add_log(
    level="ERROR",
    message="Failed login attempt",
    ip_address="192.168.1.10"
)

analyzer.add_log(
    level="WARNING",
    message="High memory usage",
    ip_address="10.0.0.5"
)

report = analyzer.generate_report()