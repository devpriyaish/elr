# Employee Leave Requests
This is a FastAPI-based RESTful API for managing leave requests in an organization.

## **📌 Installation & Setup**
### **1 Clone the Repository**
```bash
git clone git@github.com:devpriyaish/elr.git
cd elm/elm
```

### **2 Install Dependencies**
```bash
pip install -r requirements.txt
```

### **3 Run the FastAPI Server**
```bash
uvicorn main:app --reload
```

### **4 Access API Docs**
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)  
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)  

## **📌 API Endpoints**
### **1 Create a Leave Request**
```http
POST /api/v1/leave-requests
```
#### **Request Body (JSON)**
```json
{
  "employee_id": "12345",
  "start_date": "2024-03-10",
  "end_date": "2024-03-15",
  "leave_type": "sick",
  "reason": "Medical emergency"
}
```
#### **Response**
```json
{
  "id": "1",
  "employee_id": "12345",
  "start_date": "2024-03-10",
  "end_date": "2024-03-15",
  "leave_type": "sick",
  "reason": "Medical emergency",
  "status": "pending",
  "working_days": 5,
  "created_at": "2024-03-04T12:00:00Z"
}
```

## **📌 License**
MIT License  