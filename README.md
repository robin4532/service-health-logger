# Service Health Logger

Service Health Logger is a lightweight backend service designed to record
health signals and incidents from running services in a cloud-native
environment.
The project focuses on the reliability layer of modern systems, where
understanding failures and service behavior over time is critical.

# Why I Decided to Build this project

In real-world production systems, failures are inevitable. What matters
is how quickly teams can detect issues, understand impact, and respond.
This project explores the foundational ideas behind:
- service health monitoring
- incident logging
- system reliability and observability

## What This Service Does

- Allows services to register themselves
- Accepts health status signals (up / down)
- Logs incidents with timestamps
- Exposes APIs to query service health history

The design is intentionally simple and API-first.

## Tech Stack

- Python
- FastAPI
- (Database and infrastructure added incrementally)

# Current Status

It is an early stage prototype built to explore cloud-native and
infrastructure concepts from the ground up.

# Future Implementatons 

- Persistent storage (PostgreSQL)
- Containerization with Docker
- Kubernetes deployment configuration
- Integration with alerting or monitoring tools
