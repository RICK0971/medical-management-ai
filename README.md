# 🏥 Medical Management AI

A full-stack AI-powered medical management system built with Pydantic AI, FastAPI, and Next.js.

## Features

- 💊 **Medication Management** - Track medications, dosages, and schedules
- 📅 **Appointment Tracking** - Manage doctor appointments and medical visits
- 📊 **Health Metrics** - Log and visualize vital signs (BP, sugar, weight, etc.)
- 🤖 **AI Health Assistant** - Chat with an AI agent for medical guidance
- 📄 **Document Storage** - Upload and organize prescriptions and lab reports

## Tech Stack

### Backend
- **FastAPI** - Modern Python web framework
- **Pydantic AI** - AI agent orchestration
- **PostgreSQL** - Database (Supabase)
- **Groq** - LLM provider (llama-3.1-70b)

### Frontend
- **Next.js 14** - React framework with App Router
- **Tailwind CSS** - Styling
- **shadcn/ui** - UI components
- **Recharts** - Data visualization

## Quick Start

### Prerequisites
- Python 3.11+
- Node.js 18+
- PostgreSQL (or Supabase account)
- Groq API key (free at https://console.groq.com)

### Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up environment variables
cp .env.example .env
# Edit .env with your credentials

# Run database migrations
python -m app.services.database

# Start server
uvicorn main:app --reload
```

Backend will run at `http://localhost:8000`

### Frontend Setup

```bash
cd frontend

# Install dependencies
npm install

# Set up environment variables
cp .env.local.example .env.local
# Edit .env.local with your API URL

# Run development server
npm run dev
```

Frontend will run at `http://localhost:3000`

## Environment Variables

### Backend (.env)
```
DATABASE_URL=postgresql://user:password@localhost:5432/medical_db
GROQ_API_KEY=your_groq_api_key
SECRET_KEY=your_secret_key_for_jwt
SUPABASE_URL=your_supabase_url
SUPABASE_KEY=your_supabase_key
```

### Frontend (.env.local)
```
NEXT_PUBLIC_API_URL=http://localhost:8000
```

## Deployment

### Backend (Railway)
1. Push code to GitHub
2. Connect Railway to your repo
3. Add environment variables
4. Deploy automatically

### Frontend (Vercel)
1. Push code to GitHub
2. Import project in Vercel
3. Add environment variables
4. Deploy automatically

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for detailed instructions.

## Project Structure

```
├── backend/          # FastAPI backend
│   ├── app/
│   │   ├── agents/   # Pydantic AI agents
│   │   ├── api/      # API routes
│   │   ├── models/   # Data models
│   │   └── services/ # Business logic
│   └── main.py
│
├── frontend/         # Next.js frontend
│   ├── app/          # App router pages
│   ├── components/   # React components
│   └── lib/          # Utilities
│
└── database/         # SQL schemas
```

## API Documentation

Once the backend is running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Features Roadmap

- [x] Medication tracking
- [x] Appointment management
- [x] Health metrics logging
- [x] AI chat assistant
- [ ] Document OCR
- [ ] Medication reminders
- [ ] Export health reports
- [ ] Multi-language support

## Contributing

This is a student project for educational purposes.

## License

MIT License

## Author

Built for Full Stack AI Agent Development course.

---

**⚠️ Medical Disclaimer**: This application is for educational purposes only and should not be used as a substitute for professional medical advice, diagnosis, or treatment.
