from collections import defaultdict
from datetime import datetime


class URLShortener:
    """
    Basic URL shortening service logic.
    Similar to bit.ly or tinyurl systems.
    """

    def __init__(self):
        self.url_database = {}
        self.click_analytics = defaultdict(list)
        self.counter = 1000

    def shorten_url(self, original_url):
        """
        Generate a short code for a URL.

        Returns:
            dict
        """

        short_code = f"url{self.counter}"

        self.url_database[short_code] = original_url

        self.counter += 1

        return {
            "short_code": short_code,
            "short_url": f"https://sho.rt/{short_code}"
        }

    def resolve_url(self, short_code, visitor_ip):
        """
        Resolve short URL back to original URL
        and track analytics.
        """

        if short_code not in self.url_database:
            return {
                "success": False,
                "message": "URL not found"
            }

        self.click_analytics[short_code].append({
            "ip": visitor_ip,
            "timestamp": datetime.now()
        })

        return {
            "success": True,
            "original_url": (
                self.url_database[short_code]
            )
        }

    def get_analytics(self, short_code):
        """
        Return analytics for a short URL.
        """

        visits = self.click_analytics[short_code]

        unique_ips = {
            visit["ip"]
            for visit in visits
        }

        return {
            "total_clicks": len(visits),
            "unique_visitors": len(unique_ips),
            "visit_logs": visits
        }


# Example usage
service = URLShortener()

shortened = service.shorten_url(
    "https://www.example.com/python-course"
)

service.resolve_url(
    short_code=shortened["short_code"],
    visitor_ip="192.168.1.5"
)

service.resolve_url(
    short_code=shortened["short_code"],
    visitor_ip="192.168.1.5"
)

service.resolve_url(
    short_code=shortened["short_code"],
    visitor_ip="10.0.0.2"
)

analytics = service.get_analytics(
    shortened["short_code"]
)