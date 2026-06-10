from collections import defaultdict


class LoadBalancer:
    """
    Round Robin Load Balancer.

    Distributes requests evenly
    across multiple servers.
    """

    def __init__(self):
        self.servers = []
        self.current_index = 0
        self.request_counts = defaultdict(int)

    def add_server(
        self,
        server_id
    ):
        """
        Register a server.
        """

        self.servers.append(server_id)

        return {
            "server_id": server_id,
            "status": "ACTIVE"
        }

    def remove_server(
        self,
        server_id
    ):
        """
        Remove a server.
        """

        if server_id not in self.servers:
            return {
                "success": False
            }

        self.servers.remove(server_id)

        return {
            "success": True
        }

    def route_request(
        self,
        request_id
    ):
        """
        Assign request to next server.
        """

        if not self.servers:
            return {
                "success": False,
                "message": "No servers available"
            }

        server = self.servers[
            self.current_index
        ]

        self.request_counts[server] += 1

        self.current_index = (
            self.current_index + 1
        ) % len(self.servers)

        return {
            "request_id": request_id,
            "server": server
        }

    def statistics(self):
        """
        Server utilization report.
        """

        return {
            "servers": self.servers,
            "requests_processed": dict(
                self.request_counts
            )
        }


# Example usage
lb = LoadBalancer()

lb.add_server("web-01")
lb.add_server("web-02")
lb.add_server("web-03")

request_1 = lb.route_request("REQ-001")
request_2 = lb.route_request("REQ-002")
request_3 = lb.route_request("REQ-003")
request_4 = lb.route_request("REQ-004")

stats = lb.statistics()