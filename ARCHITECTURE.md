# Project Architecture

Complete technical architecture of the Medical Management AI system.

## 📐 System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                         User Browser                         │
│                    (http://localhost:3000)                   │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ HTTP/HTTPS
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    Next.js Frontend                          │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  Pages: Landing, Login, Signup, Dashboard            │  │
│  │  Components: UI, Forms, Charts, Chat                 │  │
│  │  State: React Hooks, Local Storage                   │  │
│  │  Styling: Tailwind CSS + shadcn/ui                   │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                         │ REST API (axios)
                         │
┌────────────────────────▼────────────────────────────────────┐
│                    FastAPI Backend                           │
│  ┌──────────────────────────────────────────────────────┐  │
│  │  API Routes: /auth, /medications, /appointments      │  │
│  │  Middleware: CORS, Auth, Error Handling              │  │
│  │  Services: Database, Authentication                  │  │
│  └──────────────────────────────────────────────────────┘  │
│  ┌──────────────────────────────────────────────────────┐  │
│  │           Pydantic AI Agent System                   │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Medical Agent (llama-3.1-70b via Groq)        │  │  │
│  │  │  - System Prompt                               │  │  │
│  │  │  - Context Management                          │  │  │
│  │  │  - Tool Orchestration                          │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  │  ┌────────────────────────────────────────────────┐  │  │
│  │  │  Agent Tools                                   │  │  │
│  │  │  - get_medications()                           │  │  │
│  │  │  - add_medication()                            │  │  │
│  │  │  - schedule_appointment()                      │  │  │
│  │  │  - log_health_metric()                         │  │  │
│  │  │  - get_health_trends()                         │  │  │
│  │  └────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────┘  │
└────────────────────────┬────────────────────────────────────┘
                         │
                    ┌────┴────┐
                    │         │
         ┌──────────▼─┐   ┌──▼──────────┐
         │  Supabase  │   │    Groq     │
         │ PostgreSQL │   │  LLM API    │
         │  Database  │   │ (Free Tier) │
         └────────────┘   └─────────────┘
```

---

## 🏗️ Backend Architecture

### Directory Structure

```
backend/
├── app/
│   ├── agents/              # Pydantic AI agents
│   │   ├── __init__.py
│   │   ├── medical_agent.py # Main AI agent
│   │   └── tools.py         # Agent tools/functions
│   │
│   ├── api/                 # API route handlers
│   │   ├── __init__.py
│   │   ├── auth.py          # Authentication endpoints
│   │   ├── medications.py   # Medication CRUD
│   │   ├── appointments.py  # Appointment CRUD
│   │   ├── health_metrics.py# Health metrics CRUD
│   │   └── chat.py          # AI chat endpoint
│   │
│   ├── models/              # Pydantic data models
│   │   ├── __init__.py
│   │   ├── user.py          # User models
│   │   ├── medication.py    # Medication models
│   │   ├── appointment.py   # Appointment models
│   │   └── health_metric.py # Health metric models
│   │
│   ├── services/            # Business logic
│   │   ├── __init__.py
│   │   ├── database.py      # Supabase client
│   │   └── auth_service.py  # JWT & password handling
│   │
│   ├── utils/               # Utilities
│   │   ├── __init__.py
│   │   └── logger.py        # Logging configuration
│   │
│   └── config.py            # App configuration
│
├── main.py                  # FastAPI app entry point
├── requirements.txt         # Python dependencies
├── .env.example            # Environment template
└── railway.json            # Railway deployment config
```

### Request Flow

```
1. HTTP Request
   ↓
2. FastAPI Router
   ↓
3. Authentication Middleware (if protected)
   ↓
4. Route Handler (api/*.py)
   ↓
5. Business Logic (services/*.py)
   ↓
6. Database Query (Supabase)
   ↓
7. Response (Pydantic model)
```

### AI Agent Flow

```
1. User sends chat message
   ↓
2. POST /api/v1/chat
   ↓
3. chat.py handler
   ↓
4. run_medical_agent()
   ↓
5. Pydantic AI Agent
   ├─ Load system prompt
   ├─ Add user context (user_id, name)
   ├─ Process message with LLM (Groq)
   ├─ Decide which tools to call
   ├─ Execute tools (database queries)
   └─ Generate response
   ↓
6. Return response to user
```

### Authentication Flow

```
1. User signs up/logs in
   ↓
2. Password hashed with bcrypt
   ↓
3. User created in database
   ↓
4. JWT token generated
   ↓
5. Token sent to client
   ↓
6. Client stores token (localStorage)
   ↓
7. Client includes token in Authorization header
   ↓
8. Backend validates token on each request
```

---

## 🎨 Frontend Architecture

### Directory Structure

```
frontend/
├── app/                     # Next.js 14 App Router
│   ├── (auth)/             # Auth route group
│   │   ├── login/
│   │   │   └── page.tsx    # Login page
│   │   └── signup/
│   │       └── page.tsx    # Signup page
│   │
│   ├── (dashboard)/        # Dashboard route group
│   │   ├── dashboard/
│   │   │   └── page.tsx    # Main dashboard
│   │   ├── medications/
│   │   │   └── page.tsx    # Medications page
│   │   ├── appointments/
│   │   │   └── page.tsx    # Appointments page
│   │   ├── health-metrics/
│   │   │   └── page.tsx    # Health metrics page
│   │   └── chat/
│   │       └── page.tsx    # AI chat page
│   │
│   ├── layout.tsx          # Root layout
│   ├── page.tsx            # Landing page
│   └── globals.css         # Global styles
│
├── components/             # React components
│   ├── ui/                # shadcn/ui components
│   │   ├── button.tsx
│   │   ├── card.tsx
│   │   ├── input.tsx
│   │   └── ...
│   │
│   ├── dashboard/         # Dashboard components
│   │   ├── stats-card.tsx
│   │   └── recent-items.tsx
│   │
│   ├── medications/       # Medication components
│   │   ├── medication-list.tsx
│   │   └── add-medication-form.tsx
│   │
│   └── chat/             # Chat components
│       ├── chat-interface.tsx
│       └── message-bubble.tsx
│
├── lib/                   # Utilities
│   ├── api.ts            # API client (axios)
│   └── utils.ts          # Helper functions
│
├── public/               # Static assets
├── package.json          # Node dependencies
├── tailwind.config.ts    # Tailwind configuration
├── tsconfig.json         # TypeScript config
└── next.config.js        # Next.js config
```

### Component Hierarchy

```
App
├── Layout
│   ├── Header/Navigation
│   └── Main Content
│       ├── Landing Page
│       │   ├── Hero Section
│       │   ├── Features Grid
│       │   └── Footer
│       │
│       ├── Auth Pages
│       │   ├── Login Form
│       │   └── Signup Form
│       │
│       └── Dashboard
│           ├── Sidebar Navigation
│           ├── Dashboard Home
│           │   ├── Stats Cards
│           │   ├── Quick Actions
│           │   └── Recent Items
│           │
│           ├── Medications Page
│           │   ├── Medication List
│           │   ├── Add Medication Form
│           │   └── Medication Card
│           │
│           ├── Appointments Page
│           │   ├── Calendar View
│           │   ├── Appointment List
│           │   └── Add Appointment Form
│           │
│           ├── Health Metrics Page
│           │   ├── Metric Charts (Recharts)
│           │   ├── Log Metric Form
│           │   └── Metric History
│           │
│           └── Chat Page
│               ├── Chat Interface
│               ├── Message List
│               ├── Message Bubble
│               └── Input Box
```

### State Management

```
Local State (useState)
├── Form inputs
├── UI toggles (modals, dropdowns)
└── Loading states

Server State (React Query - optional)
├── Medications data
├── Appointments data
├── Health metrics data
└── Chat history

Persistent State (localStorage)
├── JWT token
├── User preferences
└── Theme settings
```

---

## 🗄️ Database Schema

### Tables

```sql
users
├── id (UUID, PK)
├── email (VARCHAR, UNIQUE)
├── name (VARCHAR)
├── password (VARCHAR, hashed)
├── created_at (TIMESTAMP)
└── updated_at (TIMESTAMP)

medications
├── id (UUID, PK)
├── user_id (UUID, FK → users.id)
├── name (VARCHAR)
├── dosage (VARCHAR)
├── frequency (VARCHAR)
├── start_date (DATE)
├── end_date (DATE, nullable)
├── notes (TEXT, nullable)
├── active (BOOLEAN)
├── created_at (TIMESTAMP)
└── updated_at (TIMESTAMP)

appointments
├── id (UUID, PK)
├── user_id (UUID, FK → users.id)
├── doctor_name (VARCHAR)
├── specialty (VARCHAR)
├── date_time (TIMESTAMP)
├── location (VARCHAR)
├── notes (TEXT, nullable)
├── status (VARCHAR: scheduled/completed/cancelled)
├── created_at (TIMESTAMP)
└── updated_at (TIMESTAMP)

health_metrics
├── id (UUID, PK)
├── user_id (UUID, FK → users.id)
├── metric_type (VARCHAR: blood_pressure/blood_sugar/weight/etc)
├── value (VARCHAR)
├── unit (VARCHAR)
├── notes (TEXT, nullable)
├── recorded_at (TIMESTAMP)
└── created_at (TIMESTAMP)

chat_messages (optional)
├── id (UUID, PK)
├── user_id (UUID, FK → users.id)
├── role (VARCHAR: user/assistant)
├── content (TEXT)
└── created_at (TIMESTAMP)
```

### Relationships

```
users (1) ──< (many) medications
users (1) ──< (many) appointments
users (1) ──< (many) health_metrics
users (1) ──< (many) chat_messages
```

### Indexes

```sql
-- Performance optimization
CREATE INDEX idx_medications_user_id ON medications(user_id);
CREATE INDEX idx_medications_active ON medications(active);
CREATE INDEX idx_appointments_user_id ON appointments(user_id);
CREATE INDEX idx_appointments_date_time ON appointments(date_time);
CREATE INDEX idx_health_metrics_user_id ON health_metrics(user_id);
CREATE INDEX idx_health_metrics_type ON health_metrics(metric_type);
```

---

## 🤖 Pydantic AI Agent Architecture

### Agent Components

```python
MedicalAgent
├── Model: llama-3.1-70b-versatile (Groq)
├── System Prompt: Medical assistant guidelines
├── Context: MedicalContext (user_id, user_name)
├── Tools:
│   ├── get_medications()
│   ├── add_medication()
│   ├── get_appointments()
│   ├── schedule_appointment()
│   ├── log_health_metric()
│   └── get_health_trends()
└── Retries: 2
```

### Tool Execution Flow

```
1. User: "What medications am I taking?"
   ↓
2. Agent receives message + context
   ↓
3. LLM decides to call get_medications()
   ↓
4. Tool executes database query
   ↓
5. Tool returns medication list
   ↓
6. LLM formats response naturally
   ↓
7. User receives: "You are currently taking Aspirin 100mg..."
```

### Context Management

```python
class MedicalContext(BaseModel):
    user_id: str      # For database queries
    user_name: str    # For personalization

# Passed to every tool call
async def get_medications(ctx: RunContext[MedicalContext]):
    user_id = ctx.deps.user_id  # Access user context
    # Query database for this user's medications
```

---

## 🔐 Security Architecture

### Authentication

```
Password Security
├── Hashing: bcrypt
├── Salt: Auto-generated per password
└── Rounds: 12 (default)

JWT Tokens
├── Algorithm: HS256
├── Secret: 32+ character random string
├── Expiry: 30 minutes (configurable)
└── Payload: { sub: user_id, exp: timestamp }
```

### Authorization

```
Protected Routes
├── Middleware: get_current_user()
├── Token Validation: JWT decode + verify
├── User Lookup: Database query
└── Access Control: User can only access own data
```

### Data Protection

```
Row Level Security (RLS)
├── Enabled on all tables
├── Policy: Users can only access their own rows
└── Enforced at database level (Supabase)

CORS
├── Allowed Origins: Frontend URL only
├── Credentials: Allowed
└── Methods: GET, POST, PATCH, DELETE
```

---

## 📊 Data Flow Examples

### Creating a Medication

```
Frontend                Backend                 Database
   │                       │                       │
   │  POST /medications    │                       │
   ├──────────────────────>│                       │
   │                       │  Validate JWT         │
   │                       ├───────────────────────┤
   │                       │  Validate data        │
   │                       │  (Pydantic)           │
   │                       │                       │
   │                       │  INSERT medication    │
   │                       ├──────────────────────>│
   │                       │                       │
   │                       │  Return new record    │
   │                       │<──────────────────────┤
   │  201 Created          │                       │
   │<──────────────────────┤                       │
   │  { id, name, ... }    │                       │
```

### AI Chat Interaction

```
Frontend                Backend                 Groq API              Database
   │                       │                       │                     │
   │  POST /chat           │                       │                     │
   ├──────────────────────>│                       │                     │
   │  { message: "..." }   │                       │                     │
   │                       │  Validate JWT         │                     │
   │                       │                       │                     │
   │                       │  Get user context     │                     │
   │                       ├─────────────────────────────────────────────>│
   │                       │                       │                     │
   │                       │  Run agent            │                     │
   │                       ├──────────────────────>│                     │
   │                       │  (message + context)  │                     │
   │                       │                       │                     │
   │                       │  LLM decides to call  │                     │
   │                       │  get_medications()    │                     │
   │                       │                       │                     │
   │                       │  Query medications    │                     │
   │                       ├─────────────────────────────────────────────>│
   │                       │                       │                     │
   │                       │  Return medications   │                     │
   │                       │<─────────────────────────────────────────────┤
   │                       │                       │                     │
   │                       │  LLM generates response                     │
   │                       │<──────────────────────┤                     │
   │                       │                       │                     │
   │  200 OK               │                       │                     │
   │<──────────────────────┤                       │                     │
   │  { response: "..." }  │                       │                     │
```

---

## 🚀 Deployment Architecture

### Production Setup

```
┌─────────────────────────────────────────────────────────┐
│                    Vercel (Frontend)                     │
│  - Next.js SSR/SSG                                      │
│  - Edge Network (CDN)                                   │
│  - Auto HTTPS                                           │
│  - Environment Variables                                │
└────────────────────┬────────────────────────────────────┘
                     │
                     │ HTTPS
                     │
┌────────────────────▼────────────────────────────────────┐
│                 Railway (Backend)                        │
│  - FastAPI Server                                       │
│  - Auto Scaling                                         │
│  - Health Checks                                        │
│  - Environment Variables                                │
└────────────────────┬────────────────────────────────────┘
                     │
              ┌──────┴──────┐
              │             │
┌─────────────▼──┐   ┌──────▼──────┐
│   Supabase     │   │    Groq     │
│  (Database)    │   │  (LLM API)  │
│  - PostgreSQL  │   │  - Managed  │
│  - Auto Backup │   │  - Rate     │
│  - Monitoring  │   │    Limited  │
└────────────────┘   └─────────────┘
```

---

## 📈 Scalability Considerations

### Current Limitations

- Single server instance
- No caching layer
- No rate limiting
- Synchronous AI calls

### Future Improvements

```
1. Caching
   ├── Redis for session storage
   ├── Cache frequent database queries
   └── Cache LLM responses

2. Rate Limiting
   ├── Per-user limits
   ├── Per-endpoint limits
   └── API key management

3. Async Processing
   ├── Background jobs (Celery)
   ├── Message queue (RabbitMQ)
   └── Async AI calls

4. Monitoring
   ├── Error tracking (Sentry)
   ├── Performance monitoring (New Relic)
   └── Logging (ELK stack)

5. Load Balancing
   ├── Multiple backend instances
   ├── Database read replicas
   └── CDN for static assets
```

---

## 🧪 Testing Strategy

### Backend Tests

```python
# Unit Tests
tests/
├── test_auth.py          # Authentication logic
├── test_medications.py   # Medication CRUD
├── test_agent.py         # AI agent tools
└── test_models.py        # Pydantic models

# Integration Tests
├── test_api_auth.py      # Auth endpoints
├── test_api_medications.py
└── test_api_chat.py

# Run tests
pytest tests/ -v
```

### Frontend Tests

```typescript
// Unit Tests
__tests__/
├── components/
│   ├── Button.test.tsx
│   └── MedicationCard.test.tsx
└── lib/
    └── api.test.ts

// Integration Tests
├── pages/
│   ├── login.test.tsx
│   └── dashboard.test.tsx

// Run tests
npm test
```

---

## 📝 Code Quality

### Backend

```python
# Type hints
def create_medication(
    medication: MedicationCreate,
    user_id: str
) -> Medication:
    ...

# Pydantic validation
class MedicationCreate(BaseModel):
    name: str
    dosage: str
    frequency: str
    
    @validator('dosage')
    def validate_dosage(cls, v):
        # Custom validation
        return v

# Error handling
try:
    result = await db.query()
except Exception as e:
    logger.error(f"Error: {e}")
    raise HTTPException(500, "Internal error")
```

### Frontend

```typescript
// TypeScript interfaces
interface Medication {
  id: string;
  name: string;
  dosage: string;
  // ...
}

// Error boundaries
<ErrorBoundary fallback={<ErrorPage />}>
  <Dashboard />
</ErrorBoundary>

// Loading states
{isLoading ? <Skeleton /> : <MedicationList />}
```

---

This architecture is designed to be:
- ✅ **Scalable** - Can grow with user base
- ✅ **Maintainable** - Clear separation of concerns
- ✅ **Secure** - Multiple layers of security
- ✅ **Testable** - Easy to write tests
- ✅ **Deployable** - Simple deployment process
