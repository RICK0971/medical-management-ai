# 🏥 Medical Management AI

A full-stack AI-powered medical management system built with **Pydantic AI**, **FastAPI**, and **Next.js**.

[![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.109-green.svg)](https://fastapi.tiangolo.com/)
[![Next.js](https://img.shields.io/badge/Next.js-14-black.svg)](https://nextjs.org/)
[![VS Code](https://img.shields.io/badge/VS%20Code-Optimized-007ACC.svg)](https://code.visualstudio.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

> **Built for Full Stack AI Agent Development Course**
> 
> **Optimized for Visual Studio Code** 💻

---

## ✨ Features

- 💊 **Medication Management** - Track medications, dosages, and schedules with smart reminders
- 📅 **Appointment Tracking** - Manage doctor appointments and medical visits
- 📊 **Health Metrics** - Log and visualize vital signs (BP, blood sugar, weight, etc.)
- 🤖 **AI Health Assistant** - Chat with an intelligent AI agent powered by Pydantic AI
- 📄 **Document Storage** - Upload and organize prescriptions and lab reports
- 🔐 **Secure Authentication** - JWT-based auth with bcrypt password hashing
- 📱 **Responsive Design** - Beautiful UI with Tailwind CSS and shadcn/ui

---

## 🚀 Quick Start

**Get running in 5 minutes with VS Code!** → [QUICKSTART.md](QUICKSTART.md)

```bash
# Clone the repository
git clone https://github.com/RICK0971/medical-management-ai.git
cd medical-management-ai
code .  # Open in VS Code

# Backend setup
cd backend
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# Frontend setup (new terminal)
cd frontend
npm install

# Configure environment variables (see QUICKSTART.md)
# Then run both servers
```

---

## 📚 Documentation

### Getting Started
| Document | Description |
|----------|-------------|
| **[QUICKSTART.md](QUICKSTART.md)** | 5-minute setup guide for VS Code |
| **[INSTALLATION.md](INSTALLATION.md)** | Complete installation guide for VS Code |
| **[VSCODE_GUIDE.md](VSCODE_GUIDE.md)** | Comprehensive VS Code developer guide |
| **[VSCODE_QUICKREF.md](VSCODE_QUICKREF.md)** | VS Code shortcuts quick reference |

### Technical Documentation
| Document | Description |
|----------|-------------|
| **[ARCHITECTURE.md](ARCHITECTURE.md)** | System architecture and design |
| **[PACKAGES.md](PACKAGES.md)** | Complete package reference |
| **[TROUBLESHOOTING.md](TROUBLESHOOTING.md)** | Common issues and solutions |
| **[docs/SETUP.md](docs/SETUP.md)** | Detailed setup instructions |
| **[docs/API.md](docs/API.md)** | API documentation |
| **[docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)** | Production deployment guide |

---

## 🛠️ Tech Stack

### Backend
- **[FastAPI](https://fastapi.tiangolo.com/)** - Modern Python web framework
- **[Pydantic AI](https://ai.pydantic.dev/)** - AI agent orchestration framework
- **[PostgreSQL](https://www.postgresql.org/)** - Database (via Supabase)
- **[Groq](https://groq.com/)** - LLM provider (llama-3.1-70b-versatile)
- **[Supabase](https://supabase.com/)** - Backend-as-a-Service

### Frontend
- **[Next.js 14](https://nextjs.org/)** - React framework with App Router
- **[TypeScript](https://www.typescriptlang.org/)** - Type safety
- **[Tailwind CSS](https://tailwindcss.com/)** - Utility-first CSS
- **[shadcn/ui](https://ui.shadcn.com/)** - Beautiful UI components
- **[Recharts](https://recharts.org/)** - Data visualization

---

## 📋 Prerequisites

- **Python 3.11+** - [Download](https://www.python.org/downloads/)
- **Node.js 18+** - [Download](https://nodejs.org/)
- **Git** - [Download](https://git-scm.com/)
- **VS Code** - [Download](https://code.visualstudio.com/)
- **Supabase Account** - [Sign up](https://supabase.com/) (free)
- **Groq API Key** - [Get free key](https://console.groq.com/)

---

## 🎯 VS Code Setup

This project is **optimized for Visual Studio Code** with pre-configured settings.

### Automatic Setup
When you open the project in VS Code:
1. ✅ Recommended extensions prompt appears
2. ✅ Python interpreter auto-detected
3. ✅ Workspace settings applied
4. ✅ Debug configurations ready

### Recommended Extensions
The project will prompt you to install:
- **Python** (Microsoft) - Python language support
- **Pylance** (Microsoft) - Python IntelliSense
- **ESLint** (Microsoft) - JavaScript/TypeScript linting
- **Prettier** (Prettier) - Code formatting
- **Tailwind CSS IntelliSense** - Tailwind autocomplete
- **GitLens** - Git supercharged
- **Thunder Client** - API testing
- **Error Lens** - Inline errors

### Pre-configured Features
- ✅ Auto-formatting on save
- ✅ Python linting enabled
- ✅ Import organization
- ✅ Tailwind IntelliSense
- ✅ Debug configurations
- ✅ File exclusions

**Learn more:** [VSCODE_GUIDE.md](VSCODE_GUIDE.md)

---

## 🏗️ Project Structure

```
medical-management-ai/
├── .vscode/                    # VS Code configuration
│   ├── settings.json          # Workspace settings
│   ├── extensions.json        # Recommended extensions
│   └── launch.json            # Debug configurations
│
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── agents/            # Pydantic AI agents
│   │   ├── api/               # API routes
│   │   ├── models/            # Pydantic models
│   │   └── services/          # Business logic
│   └── main.py
│
├── frontend/                   # Next.js frontend
│   ├── app/                   # App router pages
│   ├── components/            # React components
│   └── lib/                   # Utilities
│
├── database/                   # Database schema
├── docs/                       # Documentation
│
├── QUICKSTART.md              # Quick start guide
├── INSTALLATION.md            # Installation guide
├── VSCODE_GUIDE.md            # VS Code developer guide
├── VSCODE_QUICKREF.md         # VS Code quick reference
├── ARCHITECTURE.md            # Architecture docs
├── PACKAGES.md                # Package reference
├── TROUBLESHOOTING.md         # Troubleshooting guide
└── README.md                  # This file
```

---

## 🎯 Key Features Explained

### 🤖 Pydantic AI Agent

The heart of the system is a Pydantic AI agent that:
- Uses **llama-3.1-70b-versatile** via Groq (fast & free)
- Has access to **6 tools** for database operations
- Maintains **user context** across conversations
- Provides **natural language** medical assistance

**Example interaction:**
```
User: "What medications am I taking?"
Agent: *calls get_medications() tool*
Agent: "You are currently taking Aspirin 100mg once daily..."
```

### 🔐 Security

- **JWT Authentication** - Secure token-based auth
- **Password Hashing** - bcrypt with auto-generated salts
- **Row Level Security** - Database-level access control
- **CORS Protection** - Configured allowed origins
- **Input Validation** - Pydantic models validate all data

### 📊 Health Tracking

Track multiple health metrics:
- Blood Pressure
- Blood Sugar
- Weight
- Temperature
- Heart Rate
- Oxygen Saturation

Visualize trends with interactive charts powered by Recharts.

---

## 🚀 Deployment

### Backend → Railway

```bash
# Push to GitHub
git push origin main

# Connect Railway to your repo
# Add environment variables
# Deploy automatically
```

### Frontend → Vercel

```bash
# Import from GitHub
# Add NEXT_PUBLIC_API_URL
# Deploy automatically
```

**Detailed guide:** [docs/DEPLOYMENT.md](docs/DEPLOYMENT.md)

---

## 📖 API Documentation

Once the backend is running, visit:
- **Swagger UI:** `http://localhost:8000/docs`
- **ReDoc:** `http://localhost:8000/redoc`

**Complete API reference:** [docs/API.md](docs/API.md)

---

## 🧪 Testing

### Backend
```bash
cd backend
pytest tests/ -v
```

### Frontend
```bash
cd frontend
npm test
```

---

## 💡 VS Code Tips

### Essential Shortcuts
- **Command Palette:** `Ctrl+Shift+P` (Mac: `Cmd+Shift+P`)
- **Toggle Terminal:** `` Ctrl+` ``
- **Quick Open:** `Ctrl+P`
- **Format Document:** `Shift+Alt+F`

### Debugging
1. Set breakpoints (click left of line number)
2. Press `F5`
3. Choose configuration (Python: FastAPI or Next.js)

### Split Terminal
1. Click terminal panel
2. Click split icon (⊞)
3. Run backend in one, frontend in other

**Full guide:** [VSCODE_GUIDE.md](VSCODE_GUIDE.md)  
**Quick reference:** [VSCODE_QUICKREF.md](VSCODE_QUICKREF.md)

---

## 🤝 Contributing

This is a student project for educational purposes. Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

---

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

---

## ⚠️ Medical Disclaimer

**IMPORTANT:** This application is for **educational purposes only** and should **not** be used as a substitute for professional medical advice, diagnosis, or treatment. Always seek the advice of your physician or other qualified health provider with any questions you may have regarding a medical condition.

---

## 🙏 Acknowledgments

- **[Pydantic AI](https://ai.pydantic.dev/)** - Amazing AI agent framework
- **[FastAPI](https://fastapi.tiangolo.com/)** - Best Python web framework
- **[Next.js](https://nextjs.org/)** - Excellent React framework
- **[Supabase](https://supabase.com/)** - Great backend platform
- **[Groq](https://groq.com/)** - Fast & free LLM inference
- **[shadcn/ui](https://ui.shadcn.com/)** - Beautiful components
- **[VS Code](https://code.visualstudio.com/)** - Best code editor

---

## 📞 Support

- **Documentation:** Check the [docs/](docs/) folder
- **Issues:** Open an issue on GitHub
- **Questions:** Review [INSTALLATION.md](INSTALLATION.md) and [QUICKSTART.md](QUICKSTART.md)
- **Troubleshooting:** See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **VS Code Help:** See [VSCODE_GUIDE.md](VSCODE_GUIDE.md)

---

## 🎓 Learning Resources

### Pydantic AI
- [Official Docs](https://ai.pydantic.dev/)
- [GitHub](https://github.com/pydantic/pydantic-ai)

### FastAPI
- [Tutorial](https://fastapi.tiangolo.com/tutorial/)
- [Advanced Guide](https://fastapi.tiangolo.com/advanced/)

### Next.js
- [Learn Next.js](https://nextjs.org/learn)
- [App Router Docs](https://nextjs.org/docs/app)

### VS Code
- [Python in VS Code](https://code.visualstudio.com/docs/python)
- [JavaScript in VS Code](https://code.visualstudio.com/docs/languages/javascript)

---

## 🗺️ Roadmap

- [ ] Document OCR for prescriptions
- [ ] Medication reminder notifications
- [ ] Export health reports as PDF
- [ ] Multi-language support
- [ ] Mobile app (React Native)
- [ ] Integration with wearables
- [ ] Telemedicine features
- [ ] Family account management

---

## 📊 Project Stats

- **Backend:** ~2,000 lines of Python
- **Frontend:** ~3,000 lines of TypeScript/TSX
- **Database:** 5 tables with RLS
- **API Endpoints:** 20+
- **AI Tools:** 6 agent tools
- **Dependencies:** 40+ packages
- **Documentation:** 10+ guides

---

## 🌟 Star History

If you find this project helpful, please consider giving it a star! ⭐

---

**Built with ❤️ for the Full Stack AI Agent Development course**

**Optimized for Visual Studio Code** 💻

Repository: [github.com/RICK0971/medical-management-ai](https://github.com/RICK0971/medical-management-ai)
