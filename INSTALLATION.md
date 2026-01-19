# Installation Guide for VS Code

Complete step-by-step guide to run this project in Visual Studio Code.

## 📋 Prerequisites

Before you begin, install these on your system:

### 1. Python 3.11+
**Windows:**
- Download from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during installation
- Verify: Open CMD and run `python --version`

**macOS:**
```bash
brew install python@3.11
```

**Linux:**
```bash
sudo apt update
sudo apt install python3.11 python3.11-venv python3-pip
```

### 2. Node.js 18+
**Windows/macOS:**
- Download from [nodejs.org](https://nodejs.org/)
- Install LTS version

**Linux:**
```bash
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt-get install -y nodejs
```

Verify: `node --version` and `npm --version`

### 3. Git
**Windows:**
- Download from [git-scm.com](https://git-scm.com/)

**macOS:**
```bash
brew install git
```

**Linux:**
```bash
sudo apt install git
```

### 4. Visual Studio Code
- Download from [code.visualstudio.com](https://code.visualstudio.com/)
- Install and open

---

## 🚀 Quick Start (5 Minutes)

### Step 1: Clone in VS Code

**Method 1: Using Command Palette**
1. Open VS Code
2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac)
3. Type "Git: Clone" and press Enter
4. Paste: `https://github.com/RICK0971/medical-management-ai.git`
5. Choose a folder to save the project
6. Click "Open" when prompted

**Method 2: Using Terminal**
```bash
git clone https://github.com/RICK0971/medical-management-ai.git
cd medical-management-ai
code .
```

### Step 2: Install VS Code Extensions

VS Code will prompt you to install recommended extensions. Click "Install All" or install manually:

**Required Extensions:**
1. **Python** (Microsoft) - `ms-python.python`
2. **Pylance** (Microsoft) - `ms-python.vscode-pylance`
3. **ESLint** (Microsoft) - `dbaeumer.vscode-eslint`
4. **Prettier** (Prettier) - `esbenp.prettier-vscode`

**Recommended Extensions:**
5. **Tailwind CSS IntelliSense** - `bradlc.vscode-tailwindcss`
6. **GitLens** - `eamodio.gitlens`
7. **Thunder Client** - `rangav.vscode-thunder-client` (API testing)
8. **Error Lens** - `usernamehw.errorlens`

**Install via Command Palette:**
```
Ctrl+Shift+P → Extensions: Install Extensions
```

### Step 3: Open Integrated Terminal

In VS Code:
- Press `` Ctrl+` `` (backtick) to open terminal
- Or go to Terminal → New Terminal
- Or View → Terminal

### Step 4: Backend Setup

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows (Command Prompt):
venv\Scripts\activate

# On Windows (PowerShell):
venv\Scripts\Activate.ps1

# On macOS/Linux:
source venv/bin/activate

# Install all packages
pip install -r requirements.txt
```

**Expected output:**
```
Successfully installed fastapi-0.109.0 uvicorn-0.27.0 pydantic-ai-0.0.14 ...
```

**VS Code Python Interpreter:**
1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose the one in `./backend/venv/...`

### Step 5: Set Up Supabase (Free Database)

1. Go to [supabase.com](https://supabase.com/)
2. Click "Start your project"
3. Sign in with GitHub
4. Click "New project"
5. Fill in:
   - Name: `medical-management`
   - Database Password: (create a strong password)
   - Region: Choose closest to you
6. Click "Create new project"
7. Wait 2-3 minutes for setup

**Get your credentials:**
- Click "Settings" (gear icon) → "API"
- Copy these values:
  - Project URL
  - anon/public key
  - service_role key

**Set up database tables:**
1. Click "SQL Editor" in sidebar
2. In VS Code, open `database/schema.sql`
3. Copy all the SQL code (`Ctrl+A`, `Ctrl+C`)
4. Paste into Supabase SQL Editor
5. Click "Run"
6. You should see "Success. No rows returned"

### Step 6: Get Groq API Key (Free AI)

1. Go to [console.groq.com](https://console.groq.com/)
2. Sign up (free)
3. Click "API Keys" in sidebar
4. Click "Create API Key"
5. Name it "medical-ai"
6. Copy the key (starts with `gsk_...`)

### Step 7: Configure Backend Environment

In VS Code:

1. Open `backend/.env.example`
2. Press `Ctrl+Shift+P`
3. Type "File: Save As"
4. Save as `backend/.env`
5. Fill in your credentials:

```env
# Paste your Supabase credentials
SUPABASE_URL=https://xxxxx.supabase.co
SUPABASE_KEY=your-anon-key-here
SUPABASE_SERVICE_KEY=your-service-role-key-here

# Paste your Groq API key
GROQ_API_KEY=gsk_xxxxxxxxxxxxx

# Generate a random secret (just type random characters, min 32)
SECRET_KEY=your-super-secret-random-string-min-32-characters-long

# Keep these as is
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=development
DEBUG=True
ALLOWED_ORIGINS=http://localhost:3000
```

### Step 8: Run Backend

In terminal (make sure you're in `backend` folder with venv activated):

```bash
uvicorn main:app --reload
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

✅ **Test it:** Open browser and go to `http://localhost:8000/docs`

You should see the API documentation!

### Step 9: Frontend Setup (New Terminal)

**Open a NEW terminal in VS Code:**
- Click the `+` icon in terminal panel
- Or press `` Ctrl+Shift+` ``
- Or Terminal → New Terminal

```bash
# Navigate to frontend
cd frontend

# Install all packages (this takes 2-3 minutes)
npm install
```

**Expected output:**
```
added 345 packages in 2m
```

### Step 10: Configure Frontend Environment

1. In VS Code, copy `frontend/.env.local.example` to `frontend/.env.local`
2. Open `.env.local`
3. It should contain:

```env
NEXT_PUBLIC_API_URL=http://localhost:8000
```

(This is already correct for local development!)

### Step 11: Run Frontend

In the frontend terminal:

```bash
npm run dev
```

**Expected output:**
```
  ▲ Next.js 14.1.0
  - Local:        http://localhost:3000
  - Ready in 2.3s
```

✅ **Test it:** Open browser and go to `http://localhost:3000`

You should see the landing page!

---

## 🎉 You're Done!

You should now have:
- ✅ Backend running on `http://localhost:8000`
- ✅ Frontend running on `http://localhost:3000`
- ✅ Database on Supabase
- ✅ AI powered by Groq

### Try It Out:

1. Go to `http://localhost:3000`
2. Click "Sign Up"
3. Create an account
4. Add a medication
5. Chat with the AI!

---

## 📦 Complete Package List

### Backend Packages (Python)

All installed via `pip install -r requirements.txt`:

```
fastapi==0.109.0              # Web framework
uvicorn[standard]==0.27.0     # ASGI server
pydantic-ai==0.0.14           # AI agent framework
pydantic==2.5.3               # Data validation
supabase==2.3.4               # Database client
groq==0.4.2                   # LLM provider
python-jose[cryptography]     # JWT tokens
passlib[bcrypt]               # Password hashing
loguru==0.7.2                 # Logging
python-dotenv==1.0.0          # Environment variables
```

### Frontend Packages (Node.js)

All installed via `npm install`:

```
next@14.1.0                   # React framework
react@18.2.0                  # UI library
typescript@5                  # Type safety
tailwindcss@3.3.0            # Styling
axios@1.6.5                   # HTTP client
lucide-react@0.323.0         # Icons
recharts@2.10.4              # Charts
@radix-ui/*                   # UI components
```

---

## 🔧 VS Code Tips & Shortcuts

### Essential Shortcuts

| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Quick Open File | `Ctrl+P` | `Cmd+P` |
| Toggle Terminal | `` Ctrl+` `` | `` Cmd+` `` |
| New Terminal | `` Ctrl+Shift+` `` | `` Cmd+Shift+` `` |
| Toggle Sidebar | `Ctrl+B` | `Cmd+B` |
| Split Editor | `Ctrl+\` | `Cmd+\` |
| Go to Definition | `F12` | `F12` |
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Save All | `Ctrl+K S` | `Cmd+K S` |

### Terminal Management

**Split Terminal:**
1. Click terminal panel
2. Click split icon (⊞) in top-right
3. Run backend in one, frontend in other

**Switch Between Terminals:**
- Click dropdown in terminal panel
- Or use `Ctrl+Shift+5` to cycle

**Kill Terminal:**
- Click trash icon
- Or type `exit`

### Python in VS Code

**Select Python Interpreter:**
```
Ctrl+Shift+P → Python: Select Interpreter
→ Choose ./backend/venv/...
```

**Run Python File:**
- Click ▶️ button in top-right
- Or press `F5`

**Python Debugging:**
1. Set breakpoint (click left of line number)
2. Press `F5`
3. Choose "Python File"

### JavaScript/TypeScript in VS Code

**Format on Save:**
1. `Ctrl+Shift+P` → "Preferences: Open Settings (JSON)"
2. Add:
```json
{
  "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode"
}
```

**Auto Import:**
- Type component name
- Press `Ctrl+Space`
- Select from suggestions

### Git in VS Code

**Source Control Panel:**
- Click Source Control icon (left sidebar)
- Or press `Ctrl+Shift+G`

**Commit Changes:**
1. Stage files (click `+`)
2. Write commit message
3. Click ✓ or press `Ctrl+Enter`

**View Git History:**
- Install GitLens extension
- Click file → View File History

---

## ❌ Common Issues & Fixes

### Issue: "python: command not found"

**Fix:**
```bash
# Try python3 instead
python3 -m venv venv
```

### Issue: "pip: command not found"

**Fix:**
```bash
# Use python -m pip
python -m pip install -r requirements.txt
```

### Issue: Cannot activate venv on Windows PowerShell

**Fix:**
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy RemoteSigned

# Then try again
venv\Scripts\Activate.ps1
```

**Or use Command Prompt instead:**
```cmd
venv\Scripts\activate
```

### Issue: "Module not found" in Python

**Fix:**
```bash
# Make sure venv is activated (you should see (venv) in terminal)
# Check Python interpreter in VS Code
Ctrl+Shift+P → Python: Select Interpreter → Choose venv

# Reinstall packages
pip install -r requirements.txt
```

### Issue: "npm install fails"

**Fix:**
```bash
# Clear cache and retry
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

### Issue: Port already in use

**Fix:**
```bash
# Kill the process
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# macOS/Linux:
lsof -ti:8000 | xargs kill -9
```

### Issue: VS Code not recognizing imports

**Fix:**
1. Reload VS Code: `Ctrl+Shift+P` → "Developer: Reload Window"
2. Check Python interpreter is selected
3. Check TypeScript version: `Ctrl+Shift+P` → "TypeScript: Select TypeScript Version"

---

## 🎯 VS Code Workspace Settings

Create `.vscode/settings.json` in project root:

```json
{
  "python.defaultInterpreterPath": "${workspaceFolder}/backend/venv/bin/python",
  "python.linting.enabled": true,
  "python.linting.pylintEnabled": true,
  "python.formatting.provider": "black",
  "editor.formatOnSave": true,
  "editor.codeActionsOnSave": {
    "source.organizeImports": true
  },
  "files.exclude": {
    "**/__pycache__": true,
    "**/*.pyc": true,
    "**/.pytest_cache": true,
    "**/node_modules": true,
    "**/.next": true
  },
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter",
    "editor.formatOnSave": true
  },
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  }
}
```

---

## 🚀 Development Workflow in VS Code

### Daily Development:

**Terminal 1 (Backend):**
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
uvicorn main:app --reload
```

**Terminal 2 (Frontend):**
```bash
cd frontend
npm run dev
```

### Making Changes:

1. **Backend changes:**
   - Edit files in `backend/app/`
   - Server auto-reloads
   - Check terminal for errors
   - Test at `http://localhost:8000/docs`

2. **Frontend changes:**
   - Edit files in `frontend/app/` or `frontend/components/`
   - Browser auto-refreshes
   - Check browser console (F12) for errors

### Debugging:

**Backend (Python):**
1. Create `.vscode/launch.json`:
```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "Python: FastAPI",
      "type": "python",
      "request": "launch",
      "module": "uvicorn",
      "args": [
        "main:app",
        "--reload"
      ],
      "cwd": "${workspaceFolder}/backend",
      "env": {
        "PYTHONPATH": "${workspaceFolder}/backend"
      }
    }
  ]
}
```
2. Set breakpoints
3. Press `F5`

**Frontend (Next.js):**
1. Add to `.vscode/launch.json`:
```json
{
  "name": "Next.js: debug",
  "type": "node",
  "request": "launch",
  "runtimeExecutable": "npm",
  "runtimeArgs": ["run", "dev"],
  "cwd": "${workspaceFolder}/frontend",
  "port": 9229
}
```
2. Press `F5`

### Stopping Servers:

- Press `Ctrl+C` in each terminal
- Or click trash icon in terminal panel

---

## 📚 Next Steps

1. **Read the docs:**
   - `docs/SETUP.md` - Detailed setup
   - `docs/API.md` - API reference
   - `docs/DEPLOYMENT.md` - Deploy to production

2. **Customize:**
   - Modify UI in `frontend/app/`
   - Add AI tools in `backend/app/agents/tools.py`
   - Update styling in `frontend/app/globals.css`

3. **Deploy:**
   - Backend → Railway
   - Frontend → Vercel
   - Follow `docs/DEPLOYMENT.md`

---

## 💡 VS Code Extensions for Better Development

### Python Development
- **Python** - Essential
- **Pylance** - IntelliSense
- **Python Indent** - Auto-indentation
- **autoDocstring** - Generate docstrings
- **Python Test Explorer** - Run tests

### JavaScript/TypeScript
- **ESLint** - Linting
- **Prettier** - Code formatting
- **Auto Rename Tag** - Rename HTML tags
- **Path Intellisense** - Autocomplete paths
- **Import Cost** - Show import sizes

### General
- **GitLens** - Git supercharged
- **Thunder Client** - API testing
- **Error Lens** - Inline errors
- **Todo Tree** - Track TODOs
- **Better Comments** - Colorful comments
- **Bracket Pair Colorizer** - Colorful brackets

---

## 📞 Need Help?

1. Check the error message carefully
2. Look in the terminal for specific errors
3. Check `docs/SETUP.md` for detailed troubleshooting
4. Review API docs at `http://localhost:8000/docs`
5. Check Supabase logs in dashboard
6. See `TROUBLESHOOTING.md` for common issues

---

## ✅ Verification Checklist

Before you start developing, verify:

- [ ] Python 3.11+ installed (`python --version`)
- [ ] Node.js 18+ installed (`node --version`)
- [ ] Git installed (`git --version`)
- [ ] VS Code installed and opened
- [ ] Required extensions installed
- [ ] Project cloned successfully
- [ ] Backend venv created and activated
- [ ] Backend packages installed
- [ ] Supabase project created
- [ ] Database schema executed
- [ ] `.env` file configured
- [ ] Backend running on port 8000
- [ ] Frontend packages installed
- [ ] Frontend running on port 3000
- [ ] Can access both URLs in browser
- [ ] Can sign up and login

If all checked ✅, you're ready to develop!

---

**Happy coding in VS Code! 🎉**
