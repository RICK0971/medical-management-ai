# API Documentation

Complete API reference for the Medical Management AI backend.

Base URL: `http://localhost:8000/api/v1` (development)

## Authentication

All endpoints except `/auth/signup` and `/auth/login` require authentication.

**Authentication Header:**
```
Authorization: Bearer <your_jwt_token>
```

---

## Auth Endpoints

### Sign Up

Create a new user account.

**Endpoint:** `POST /auth/signup`

**Request Body:**
```json
{
  "email": "user@example.com",
  "name": "John Doe",
  "password": "securepassword123"
}
```

**Response:** `201 Created`
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Login

Authenticate existing user.

**Endpoint:** `POST /auth/login`

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123"
}
```

**Response:** `200 OK`
```json
{
  "user": {
    "id": "uuid",
    "email": "user@example.com",
    "name": "John Doe",
    "created_at": "2024-01-15T10:30:00Z"
  },
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

## Medications Endpoints

### Get All Medications

**Endpoint:** `GET /medications?active_only=true`

**Query Parameters:**
- `active_only` (boolean, optional): Filter active medications only (default: true)

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "name": "Aspirin",
    "dosage": "100mg",
    "frequency": "Once daily",
    "start_date": "2024-01-01",
    "end_date": null,
    "notes": "Take with food",
    "active": true,
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

### Create Medication

**Endpoint:** `POST /medications`

**Request Body:**
```json
{
  "name": "Aspirin",
  "dosage": "100mg",
  "frequency": "Once daily",
  "start_date": "2024-01-01",
  "end_date": null,
  "notes": "Take with food"
}
```

**Response:** `201 Created`
```json
{
  "id": "uuid",
  "user_id": "uuid",
  "name": "Aspirin",
  "dosage": "100mg",
  "frequency": "Once daily",
  "start_date": "2024-01-01",
  "end_date": null,
  "notes": "Take with food",
  "active": true,
  "created_at": "2024-01-15T10:30:00Z"
}
```

### Update Medication

**Endpoint:** `PATCH /medications/{medication_id}`

**Request Body:** (all fields optional)
```json
{
  "dosage": "200mg",
  "frequency": "Twice daily",
  "notes": "Updated instructions"
}
```

**Response:** `200 OK`

### Delete Medication

**Endpoint:** `DELETE /medications/{medication_id}`

**Response:** `204 No Content`

---

## Appointments Endpoints

### Get All Appointments

**Endpoint:** `GET /appointments`

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "doctor_name": "Dr. Smith",
    "specialty": "Cardiology",
    "date_time": "2024-02-01T14:30:00Z",
    "location": "City Hospital, Room 301",
    "notes": "Annual checkup",
    "status": "scheduled",
    "created_at": "2024-01-15T10:30:00Z"
  }
]
```

### Create Appointment

**Endpoint:** `POST /appointments`

**Request Body:**
```json
{
  "doctor_name": "Dr. Smith",
  "specialty": "Cardiology",
  "date_time": "2024-02-01T14:30:00Z",
  "location": "City Hospital, Room 301",
  "notes": "Annual checkup"
}
```

**Response:** `201 Created`

### Update Appointment

**Endpoint:** `PATCH /appointments/{appointment_id}`

**Request Body:** (all fields optional)
```json
{
  "date_time": "2024-02-01T15:00:00Z",
  "status": "completed"
}
```

**Response:** `200 OK`

### Delete Appointment

**Endpoint:** `DELETE /appointments/{appointment_id}`

**Response:** `204 No Content`

---

## Health Metrics Endpoints

### Get All Health Metrics

**Endpoint:** `GET /health-metrics?metric_type=blood_pressure`

**Query Parameters:**
- `metric_type` (string, optional): Filter by metric type

**Metric Types:**
- `blood_pressure`
- `blood_sugar`
- `weight`
- `temperature`
- `heart_rate`
- `oxygen_saturation`

**Response:** `200 OK`
```json
[
  {
    "id": "uuid",
    "user_id": "uuid",
    "metric_type": "blood_pressure",
    "value": "120/80",
    "unit": "mmHg",
    "notes": "Morning reading",
    "recorded_at": "2024-01-15T08:00:00Z",
    "created_at": "2024-01-15T08:05:00Z"
  }
]
```

### Create Health Metric

**Endpoint:** `POST /health-metrics`

**Request Body:**
```json
{
  "metric_type": "blood_pressure",
  "value": "120/80",
  "unit": "mmHg",
  "notes": "Morning reading",
  "recorded_at": "2024-01-15T08:00:00Z"
}
```

**Response:** `201 Created`

### Delete Health Metric

**Endpoint:** `DELETE /health-metrics/{metric_id}`

**Response:** `204 No Content`

---

## Chat Endpoint

### Send Message to AI

**Endpoint:** `POST /chat`

**Request Body:**
```json
{
  "message": "What medications am I currently taking?"
}
```

**Response:** `200 OK`
```json
{
  "response": "You are currently taking Aspirin 100mg once daily. You started this medication on January 1st, 2024. The notes indicate you should take it with food. Is there anything specific you'd like to know about your medications?"
}
```

---

## Error Responses

### 400 Bad Request
```json
{
  "detail": "Invalid input data"
}
```

### 401 Unauthorized
```json
{
  "detail": "Could not validate credentials"
}
```

### 404 Not Found
```json
{
  "detail": "Resource not found"
}
```

### 500 Internal Server Error
```json
{
  "detail": "Internal server error"
}
```

---

## Rate Limiting

Currently no rate limiting is implemented. For production, consider adding:

```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)

@app.get("/api/v1/medications")
@limiter.limit("100/minute")
async def get_medications():
    ...
```

---

## Interactive API Documentation

Once the backend is running, visit:

- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

These provide interactive API documentation where you can test endpoints directly.

---

## Example Usage (JavaScript)

```javascript
// Login
const loginResponse = await fetch('http://localhost:8000/api/v1/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({
    email: 'user@example.com',
    password: 'password123'
  })
});

const { access_token } = await loginResponse.json();

// Get medications
const medsResponse = await fetch('http://localhost:8000/api/v1/medications', {
  headers: {
    'Authorization': `Bearer ${access_token}`
  }
});

const medications = await medsResponse.json();
console.log(medications);
```

---

## Example Usage (Python)

```python
import requests

# Login
response = requests.post(
    'http://localhost:8000/api/v1/auth/login',
    json={
        'email': 'user@example.com',
        'password': 'password123'
    }
)

token = response.json()['access_token']

# Get medications
response = requests.get(
    'http://localhost:8000/api/v1/medications',
    headers={'Authorization': f'Bearer {token}'}
)

medications = response.json()
print(medications)
```
