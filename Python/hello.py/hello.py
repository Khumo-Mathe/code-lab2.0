from collections import defaultdict
from datetime import datetime


def analyze_login_attempts(logs):
    """
    Analyze login attempts and detect suspicious activity.

    Args:
        logs (list): List of dictionaries containing:
            {
                "username": str,
                "ip": str,
                "status": "SUCCESS" or "FAILED",
                "timestamp": "YYYY-MM-DD HH:MM:SS"
            }

    Returns:
        dict: Summary of suspicious login behavior.
    """

    failed_attempts = defaultdict(int)
    suspicious_ips = set()
    successful_logins = []

    for log in logs:
        username = log["username"]
        ip = log["ip"]
        status = log["status"]

        timestamp = datetime.strptime(
            log["timestamp"],
            "%Y-%m-%d %H:%M:%S"
        )

        if status == "FAILED":
            failed_attempts[ip] += 1

            # Mark IP as suspicious after 3 failed attempts
            if failed_attempts[ip] >= 3:
                suspicious_ips.add(ip)

        elif status == "SUCCESS":
            successful_logins.append({
                "username": username,
                "ip": ip,
                "time": timestamp
            })

    return {
        "suspicious_ips": list(suspicious_ips),
        "failed_attempts": dict(failed_attempts),
        "successful_logins": successful_logins
    }


# Example usage
sample_logs = [
    {
        "username": "khumo",
        "ip": "192.168.1.10",
        "status": "FAILED",
        "timestamp": "2026-05-11 10:00:00"
    },
    {
        "username": "khumo",
        "ip": "192.168.1.10",
        "status": "FAILED",
        "timestamp": "2026-05-11 10:01:00"
    },
    {
        "username": "khumo",
        "ip": "192.168.1.10",
        "status": "FAILED",
        "timestamp": "2026-05-11 10:02:00"
    },
    {
        "username": "admin",
        "ip": "10.0.0.5",
        "status": "SUCCESS",
        "timestamp": "2026-05-11 10:05:00"
    }
]

result = analyze_login_attempts(sample_logs)