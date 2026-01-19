# 🚀 Quick Start Guide

Get the Medical Management AI running in **5 minutes**!

## ⚡ Prerequisites (2 minutes)

Install these first:
- **Python 3.11+** → [python.org/downloads](https://www.python.org/downloads/)
- **Node.js 18+** → [nodejs.org](https://nodejs.org/)
- **Git** → [git-scm.com](https://git-scm.com/)

## 📥 Step 1: Clone & Open (30 seconds)

```bash
git clone https://github.com/RICK0971/medical-management-ai.git
cd medical-management-ai
```

Open in your favorite IDE (VS Code, Cursor, etc.)

## 🔧 Step 2: Backend Setup (2 minutes)

```bash
cd backend

# Create & activate virtual environment
python -m venv venv

# Windows:
venv\Scripts\activate

# macOS/Linux:
source venv/bin/activate

# Install packages
pip install -r requirements.txt
```

## 🗄️ Step 3: Database Setup (1 minute)

1. Go to [supabase.com](https://supabase.com/) → Sign up (free)
2. Create new project → Wait 2 minutes
3. Go to SQL Editor → Copy & paste `database/schema.sql` → Run
4. Go to Settings → API → Copy your credentials

## 🔑 Step 4: Get API Keys (1 minute)

**Groq (Free AI):**
1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up → API Keys → Create → Copy

## ⚙️ Step 5: Configure Backend (30 seconds)

Copy `backend/.env.example` to `backend/.env` and fill in:

```env
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-key
GROQ_API_KEY=gsk_xxxxx
SECRET_KEY=any-random-32-character-string-here
ALLOWED_ORIGINS=http://localhost:3000
```

## ▶️ Step 6: Run Backend (10 seconds)

```bash
# In backend folder with venv activated
uvicorn main:app --reload
```

✅ Test: Open [localhost:8000/docs](http://localhost:8000/docs)

## 🎨 Step 7: Frontend Setup (1 minute)

**Open NEW terminal:**

```bash
cd frontend

# Install packages
npm install

# Copy env file
cp .env.local.example .env.local
```

## ▶️ Step 8: Run Frontend (10 seconds)

```bash
npm run dev
```

✅ Test: Open [localhost:3000](http://localhost:3000)

## 🎉 Done!

You should see:
- ✅ Backend API docs at `http://localhost:8000/docs`
- ✅ Frontend app at `http://localhost:3000`

### Try it:
1. Click "Sign Up"
2. Create account
3. Add a medication
4. Chat with AI!

---

## 📚 Next Steps

- **Full Setup Guide:** [INSTALLATION.md](INSTALLATION.md)
- **API Reference:** [docs/API.md](docs/API.md)
- **Deploy to Production:** [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)
- **Architecture Details:** [ARCHITECTURE.md](ARCHITECTURE.md)

---

## ❌ Issues?

### Backend won't start
```bash
# Make sure venv is activated (you should see (venv) in terminal)
# Reinstall packages
pip install -r requirements.txt
```

### Frontend won't start
```bash
# Clear and reinstall
rm -rf node_modules package-lock.json
npm install
```

### Database connection error
- Check `.env` credentials
- Verify Supabase project is active
- Make sure you ran `schema.sql`

### Groq API error
- Verify API key is correct
- Check you have free credits
- Try generating new key

---

## 💡 Development Tips

**Two terminals:**
1. Backend: `cd backend && uvicorn main:app --reload`
2. Frontend: `cd frontend && npm run dev`

**Stop servers:**
- Press `Ctrl+C` in each terminal

**View logs:**
- Backend: Check terminal output
- Frontend: Check browser console (F12)

---

## 📦 What's Installed?

### Backend (Python)
- FastAPI - Web framework
- Pydantic AI - AI agent system
- Supabase - Database client
- Groq - LLM provider
- JWT - Authentication

### Frontend (Node.js)
- Next.js 14 - React framework
- Tailwind CSS - Styling
- shadcn/ui - Components
- Axios - HTTP client
- Recharts - Charts

---

## 🎯 Project Structure

```
medical-management-ai/
├── backend/           # FastAPI + Pydantic AI
│   ├── app/
│   │   ├── agents/   # AI agent
│   │   ├── api/      # Routes
│   │   ├── models/   # Data models
│   │   └── services/ # Business logic
│   └── main.py
│
├── frontend/         # Next.js
│   ├── app/         # Pages
│   ├── components/  # UI components
│   └── lib/         # Utilities
│
├── database/        # SQL schema
└── docs/           # Documentation
```

---

## 🚀 Deploy to Production

**Backend → Railway:**
1. Push to GitHub
2. Connect Railway
3. Add environment variables
4. Deploy

**Frontend → Vercel:**
1. Import from GitHub
2. Add `NEXT_PUBLIC_API_URL`
3. Deploy

See [DEPLOYMENT.md](docs/DEPLOYMENT.md) for details.

---

## 📞 Need Help?

1. Check error messages in terminal
2. Review [INSTALLATION.md](INSTALLATION.md)
3. Check API docs at `localhost:8000/docs`
4. Review [ARCHITECTURE.md](ARCHITECTURE.md)

---

**Happy coding! 🎉**
