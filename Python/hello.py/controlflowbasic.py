from datetime import datetime
import hashlib


class FileIntegrityMonitor:
    """
    Detect file modifications using hashing.
    Similar to systems used in cybersecurity
    and server monitoring.
    """

    def __init__(self):
        self.file_registry = {}

    def generate_hash(self, content):
        """
        Generate SHA256 hash of file content.
        """

        return hashlib.sha256(
            content.encode()
        ).hexdigest()

    def register_file(self, filename, content):
        """
        Register a file and store its hash.
        """

        file_hash = self.generate_hash(content)

        self.file_registry[filename] = {
            "hash": file_hash,
            "last_checked": datetime.now()
        }

        return {
            "filename": filename,
            "hash": file_hash
        }

    def verify_file(self, filename, current_content):
        """
        Verify whether file has changed.
        """

        if filename not in self.file_registry:
            return {
                "success": False,
                "message": "File not registered"
            }

        current_hash = self.generate_hash(
            current_content
        )

        original_hash = (
            self.file_registry[filename]["hash"]
        )

        file_modified = (
            current_hash != original_hash
        )

        self.file_registry[filename][
            "last_checked"
        ] = datetime.now()

        return {
            "filename": filename,
            "modified": file_modified,
            "original_hash": original_hash,
            "current_hash": current_hash
        }

    def get_registered_files(self):
        """
        Return all monitored files.
        """

        return list(self.file_registry.keys())


# Example usage
monitor = FileIntegrityMonitor()

monitor.register_file(
    filename="config.txt",
    content="server_port=8080"
)

verification = monitor.verify_file(
    filename="config.txt",
    current_content="server_port=9090"
)

files = monitor.get_registered_files()