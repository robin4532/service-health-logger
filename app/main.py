from fastapi import FastAPI
from app.storage import log_incident, get_incidents

app = FastAPI(title="Service Health Logger")

@app.get("/health")
def health_check():
    return {"status": "running"}

@app.post("/incident")
def report_incident(service: str, status: str):
    log_incident(service, status)
    return {"message": "Incident logged"}

@app.get("/incidents")
def list_incidents():
    return get_incidents()
