# Setup Guide

Complete setup instructions for the Medical Management AI project.

## Prerequisites

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)
- **Supabase Account** - [Sign up](https://supabase.com/)
- **Groq API Key** - [Get free key](https://console.groq.com/)

## Step 1: Clone the Repository

```bash
git clone https://github.com/RICK0971/medical-management-ai.git
cd medical-management-ai
```

## Step 2: Backend Setup

### 2.1 Create Virtual Environment

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 2.2 Install Dependencies

```bash
pip install -r requirements.txt
```

### 2.3 Set Up Supabase Database

1. Go to [Supabase](https://supabase.com/) and create a new project
2. Wait for the database to be ready
3. Go to SQL Editor in Supabase dashboard
4. Copy the contents of `database/schema.sql`
5. Paste and run it in the SQL Editor

### 2.4 Configure Environment Variables

```bash
cp .env.example .env
```

Edit `.env` and add your credentials:

```env
# Supabase
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-key

# Groq API
GROQ_API_KEY=your-groq-api-key

# Auth (generate a random 32+ character string)
SECRET_KEY=your-super-secret-key-min-32-chars

# Environment
ENVIRONMENT=development
DEBUG=True

# CORS (add your frontend URL)
ALLOWED_ORIGINS=http://localhost:3000
```

**Where to find Supabase credentials:**
- Go to Project Settings → API
- `SUPABASE_URL` = Project URL
- `SUPABASE_KEY` = anon/public key
- `SUPABASE_SERVICE_KEY` = service_role key

**Get Groq API Key:**
- Sign up at [console.groq.com](https://console.groq.com/)
- Go to API Keys
- Create new key (free tier available)

### 2.5 Run the Backend

```bash
# Make sure you're in the backend directory with venv activated
uvicorn main:app --reload
```

Backend should now be running at `http://localhost:8000`

Test it: Open `http://localhost:8000/docs` to see the API documentation.

## Step 3: Frontend Setup

### 3.1 Install Dependencies

```bash
# Open a new terminal
cd frontend

npm install
```

### 3.2 Configure Environment

```bash
cp .env.local.example .env.local
```

Edit `.env.local`:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

### 3.3 Run the Frontend

```bash
npm run dev
```

Frontend should now be running at `http://localhost:3000`

## Step 4: Test the Application

1. Open `http://localhost:3000` in your browser
2. Click "Sign Up" and create an account
3. You should be redirected to the dashboard
4. Try adding a medication, appointment, or health metric
5. Test the AI chat feature

## Common Issues & Solutions

### Backend Issues

**Issue: `ModuleNotFoundError: No module named 'pydantic_ai'`**
```bash
# Make sure virtual environment is activated
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

**Issue: `supabase.exceptions.APIError`**
- Check your Supabase credentials in `.env`
- Make sure you ran the database schema SQL
- Verify your Supabase project is active

**Issue: `groq.APIError: Invalid API key`**
- Get a new API key from [console.groq.com](https://console.groq.com/)
- Make sure there are no extra spaces in `.env`

### Frontend Issues

**Issue: `Module not found` errors**
```bash
# Delete node_modules and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Issue: API connection errors**
- Make sure backend is running on port 8000
- Check `NEXT_PUBLIC_API_URL` in `.env.local`
- Verify CORS settings in backend `.env`

## Development Tips

### Backend Development

```bash
# Run with auto-reload
uvicorn main:app --reload

# Run on different port
uvicorn main:app --reload --port 8001

# View logs
# Logs appear in terminal with color coding
```

### Frontend Development

```bash
# Run dev server
npm run dev

# Build for production
npm run build

# Run production build
npm run start

# Lint code
npm run lint
```

### Database Management

**View data in Supabase:**
1. Go to Supabase dashboard
2. Click "Table Editor"
3. Browse your tables

**Reset database:**
1. Go to SQL Editor
2. Run: `DROP SCHEMA public CASCADE; CREATE SCHEMA public;`
3. Re-run the schema.sql file

## Next Steps

- Read [API.md](./API.md) for API documentation
- Read [DEPLOYMENT.md](./DEPLOYMENT.md) for deployment instructions
- Customize the UI in `frontend/app/`
- Add more AI agent tools in `backend/app/agents/tools.py`

## Need Help?

- Check the [README.md](../README.md)
- Review API docs at `http://localhost:8000/docs`
- Check Supabase logs in dashboard
- Review backend logs in terminal
