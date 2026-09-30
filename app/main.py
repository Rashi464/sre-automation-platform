from fastapi import FastAPI
from datetime import datetime, timezone

app = FastAPI(
    title="SRE Automation Platform",
    description="Cloud-native application for SRE and DevOps automation",
    version="1.0.0",
)


@app.get("/")
def root():
    return {
        "application": "SRE Automation Platform",
        "status": "running",
        "message": "Welcome to the SRE Automation Platform"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat()
    }


@app.get("/employees")
def get_employees():
    return [
        {"id": 1, "name": "Ananya", "role": "Software Engineer"},
        {"id": 2, "name": "Rahul", "role": "DevOps Engineer"},
        {"id": 3, "name": "Priya", "role": "SRE Engineer"},
    ]


@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):
    employees = {
        1: {"id": 1, "name": "Ananya", "role": "Software Engineer"},
        2: {"id": 2, "name": "Rahul", "role": "DevOps Engineer"},
        3: {"id": 3, "name": "Priya", "role": "SRE Engineer"},
    }

    employee = employees.get(employee_id)

    if not employee:
        return {
            "error": "Employee not found",
            "employee_id": employee_id
        }

    return employee