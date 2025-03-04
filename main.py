from datetime import datetime
from typing import List
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel


app = FastAPI()

class LeaveRequest(BaseModel):
  employee_id: str
  start_date: str
  end_date: str
  leave_type: str
  reason: str

class LeaveResponse(BaseModel):
  id: str
  employee_id: str
  start_date: str
  end_date: str
  leave_type: str
  reason: str
  status: str
  working_days: int
  created_at: str

leave_requests = {}

def calculate_working_days(start_date: str, end_date: str) -> int:
  start = datetime.strptime(start_date, "%Y-%m-%d")
  end = datetime.strptime(end_date, "%Y-%m-%d")

  if start > end:
    raise HTTPException(status_code=400, detail="Start date must be before end date")

  delta = (end - start).days + 1
  if delta > 14:
    raise HTTPException(status_code=400, detail="Maximum consecutive leave days is 14")

  return delta

  

@app.post("/api/v1/leave-requests", response_model=LeaveResponse)
async def create_leave_request(request: LeaveRequest):
  working_days = calculate_working_days(request.start_date, request.end_date)
  leave_id = f"LR{len(leave_requests) + 1:03}"
  created_at = datetime.utcnow().isoformat() + "Z"

  response = LeaveResponse(
    id=leave_id,
    employee_id=request.employee_id,
    start_date=request.start_date,
    end_date=request.end_date,
    leave_type=request.leave_type,
    reason=request.reason,
    status="PENDING",
    working_days=working_days,
    created_at=created_at
  )

  leave_requests[leave_id] = response

  return response

app.get("/api/v1/leave-requests/{employee_id}", response_model=List[LeaveResponse])
async def get_leave_requests(employee_id: str):

  results = [req for req in leave_requests.values() if req.employee_id == employee_id]
  if not results:
    raise HTTPException(status_code=404, detail="No leave requests found")
  
  return results
