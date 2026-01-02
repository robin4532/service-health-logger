#Data models for the Service Health Logger.

from typing import Dict

def create_incident(service: str, status: str, timestamp: str) -> Dict:
    """
    Create a standardized incident record.
    """
    return {
        "service": service,
        "status": status,
        "timestamp": timestamp
    }
