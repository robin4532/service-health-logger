from datetime import datetime

incidents = []

def log_incident(service_name: str, status: str):
    incidents.append({
        "service": service_name,
        "status": status,
        "timestamp": datetime.utcnow().isoformat()
    })

def get_incidents():
    return incidents
