import hashlib
import bisect

def hash_value(key: str) -> int:
    return int(hashlib.md5(key.encode()).hexdigest(), 16)

def assign_server(servers: list[str], request_id: str) -> str:
    """
    Assigns a request to a server using Consistent Hashing
    """
    # Hash servers
    server_hashes = sorted((hash_value(server), server) for server in servers)

    # Hash request
    request_hash = hash_value(request_id)

    # Find first server clockwise
    positions = [h[0] for h in server_hashes]
    index = bisect.bisect(positions, request_hash)

    # Wrap around if needed
    return server_hashes[index % len(servers)][1]



