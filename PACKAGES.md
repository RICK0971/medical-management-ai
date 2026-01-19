# 📦 Complete Package Reference

All packages and dependencies for the Medical Management AI project.

## 🐍 Backend Packages (Python)

### Installation
```bash
cd backend
pip install -r requirements.txt
```

### Core Framework (Web Server)
| Package | Version | Purpose |
|---------|---------|---------|
| `fastapi` | 0.109.0 | Modern Python web framework |
| `uvicorn[standard]` | 0.27.0 | ASGI server for FastAPI |
| `python-multipart` | 0.0.6 | Form data parsing |

### AI & LLM
| Package | Version | Purpose |
|---------|---------|---------|
| `pydantic-ai` | 0.0.14 | AI agent orchestration framework |
| `pydantic` | 2.5.3 | Data validation and settings |
| `pydantic-settings` | 2.1.0 | Settings management |
| `groq` | 0.4.2 | Groq LLM API client |
| `openai` | 1.10.0 | OpenAI API client (alternative) |

### Database
| Package | Version | Purpose |
|---------|---------|---------|
| `sqlalchemy` | 2.0.25 | SQL toolkit and ORM |
| `asyncpg` | 0.29.0 | PostgreSQL async driver |
| `alembic` | 1.13.1 | Database migrations |
| `supabase` | 2.3.4 | Supabase client library |

### Authentication & Security
| Package | Version | Purpose |
|---------|---------|---------|
| `python-jose[cryptography]` | 3.3.0 | JWT token handling |
| `passlib[bcrypt]` | 1.7.4 | Password hashing |
| `python-dotenv` | 1.0.0 | Environment variable loading |
| `email-validator` | 2.1.0 | Email validation |

### HTTP & Networking
| Package | Version | Purpose |
|---------|---------|---------|
| `httpx` | 0.26.0 | Async HTTP client |
| `aiohttp` | 3.9.1 | Async HTTP client/server |
| `python-cors` | 1.0.0 | CORS middleware |

### Utilities
| Package | Version | Purpose |
|---------|---------|---------|
| `loguru` | 0.7.2 | Advanced logging |
| `python-dateutil` | 2.8.2 | Date/time utilities |

### Testing (Optional)
| Package | Version | Purpose |
|---------|---------|---------|
| `pytest` | 7.4.4 | Testing framework |
| `pytest-asyncio` | 0.23.3 | Async test support |

---

## 📱 Frontend Packages (Node.js)

### Installation
```bash
cd frontend
npm install
```

### Core Framework
| Package | Version | Purpose |
|---------|---------|---------|
| `next` | 14.1.0 | React framework with SSR |
| `react` | 18.2.0 | UI library |
| `react-dom` | 18.2.0 | React DOM renderer |
| `typescript` | 5.x | Type safety |

### UI Components (Radix UI)
| Package | Version | Purpose |
|---------|---------|---------|
| `@radix-ui/react-dialog` | 1.0.5 | Modal dialogs |
| `@radix-ui/react-dropdown-menu` | 2.0.6 | Dropdown menus |
| `@radix-ui/react-label` | 2.0.2 | Form labels |
| `@radix-ui/react-select` | 2.0.0 | Select inputs |
| `@radix-ui/react-slot` | 1.0.2 | Slot component |
| `@radix-ui/react-tabs` | 1.0.4 | Tab navigation |
| `@radix-ui/react-toast` | 1.1.5 | Toast notifications |

### Styling
| Package | Version | Purpose |
|---------|---------|---------|
| `tailwindcss` | 3.3.0 | Utility-first CSS |
| `autoprefixer` | 10.x | CSS vendor prefixes |
| `postcss` | 8.x | CSS processing |
| `tailwindcss-animate` | 1.0.7 | Animation utilities |
| `class-variance-authority` | 0.7.0 | Component variants |
| `clsx` | 2.1.0 | Conditional classes |
| `tailwind-merge` | 2.2.1 | Merge Tailwind classes |

### Data & Charts
| Package | Version | Purpose |
|---------|---------|---------|
| `recharts` | 2.10.4 | Chart library |
| `date-fns` | 3.3.1 | Date utilities |

### HTTP & API
| Package | Version | Purpose |
|---------|---------|---------|
| `axios` | 1.6.5 | HTTP client |

### Icons
| Package | Version | Purpose |
|---------|---------|---------|
| `lucide-react` | 0.323.0 | Icon library |

### TypeScript Types
| Package | Version | Purpose |
|---------|---------|---------|
| `@types/node` | 20.x | Node.js types |
| `@types/react` | 18.x | React types |
| `@types/react-dom` | 18.x | React DOM types |

---

## 🔧 Development Tools

### Backend Development
```bash
# Code formatting
pip install black

# Linting
pip install flake8 pylint

# Type checking
pip install mypy
```

### Frontend Development
```bash
# ESLint (included in Next.js)
npm install --save-dev eslint

# Prettier
npm install --save-dev prettier

# Type checking
npm run type-check
```

---

## 📊 Package Size Comparison

### Backend
```
Total size: ~150 MB
├── FastAPI + Uvicorn: ~20 MB
├── Pydantic AI: ~30 MB
├── Supabase: ~15 MB
├── Groq: ~10 MB
├── SQLAlchemy: ~25 MB
└── Other dependencies: ~50 MB
```

### Frontend
```
Total size: ~400 MB (node_modules)
├── Next.js: ~150 MB
├── React: ~50 MB
├── Radix UI: ~80 MB
├── Tailwind CSS: ~40 MB
├── Recharts: ~30 MB
└── Other dependencies: ~50 MB

Production build: ~2-5 MB (optimized)
```

---

## 🚀 Production Dependencies Only

### Backend (Minimal)
```txt
fastapi==0.109.0
uvicorn[standard]==0.27.0
pydantic-ai==0.0.14
supabase==2.3.4
groq==0.4.2
python-jose[cryptography]==3.3.0
passlib[bcrypt]==1.7.4
python-dotenv==1.0.0
loguru==0.7.2
```

### Frontend (Minimal)
```json
{
  "dependencies": {
    "next": "14.1.0",
    "react": "18.2.0",
    "react-dom": "18.2.0",
    "axios": "1.6.5",
    "tailwindcss": "3.3.0"
  }
}
```

---

## 🔄 Update Packages

### Backend
```bash
# Check outdated packages
pip list --outdated

# Update specific package
pip install --upgrade package-name

# Update all packages (careful!)
pip install --upgrade -r requirements.txt
```

### Frontend
```bash
# Check outdated packages
npm outdated

# Update specific package
npm update package-name

# Update all packages (careful!)
npm update

# Update to latest versions
npx npm-check-updates -u
npm install
```

---

## 🐛 Common Package Issues

### Backend

**Issue: `pip install` fails**
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Try again
pip install -r requirements.txt
```

**Issue: `pydantic-ai` not found**
```bash
# Install from PyPI
pip install pydantic-ai

# Or specific version
pip install pydantic-ai==0.0.14
```

**Issue: `bcrypt` compilation error**
```bash
# Windows: Install Visual C++ Build Tools
# macOS: Install Xcode Command Line Tools
xcode-select --install

# Linux: Install build essentials
sudo apt-get install build-essential python3-dev
```

### Frontend

**Issue: `npm install` fails**
```bash
# Clear cache
npm cache clean --force

# Delete and reinstall
rm -rf node_modules package-lock.json
npm install
```

**Issue: `Module not found` errors**
```bash
# Reinstall specific package
npm install package-name

# Or reinstall all
npm install
```

**Issue: Version conflicts**
```bash
# Use legacy peer deps
npm install --legacy-peer-deps
```

---

## 📝 Package Scripts

### Backend
```bash
# Run server
uvicorn main:app --reload

# Run with specific port
uvicorn main:app --reload --port 8001

# Run tests
pytest

# Format code
black .

# Lint code
flake8 .
```

### Frontend
```bash
# Development server
npm run dev

# Production build
npm run build

# Start production server
npm run start

# Lint code
npm run lint

# Type check
npm run type-check
```

---

## 🔐 Security Updates

### Check for vulnerabilities

**Backend:**
```bash
# Check for security issues
pip-audit

# Install pip-audit first
pip install pip-audit
```

**Frontend:**
```bash
# Check for vulnerabilities
npm audit

# Fix automatically
npm audit fix

# Force fix (may break things)
npm audit fix --force
```

---

## 📦 Alternative Packages

### LLM Providers (instead of Groq)
```bash
# OpenAI
pip install openai

# Anthropic Claude
pip install anthropic

# Google Gemini
pip install google-generativeai

# Ollama (local)
pip install ollama
```

### Database (instead of Supabase)
```bash
# PostgreSQL direct
pip install psycopg2-binary

# MongoDB
pip install pymongo

# MySQL
pip install mysql-connector-python
```

### Frontend Styling (instead of Tailwind)
```bash
# Material UI
npm install @mui/material @emotion/react @emotion/styled

# Chakra UI
npm install @chakra-ui/react @emotion/react @emotion/styled

# Ant Design
npm install antd
```

---

## 💾 Freezing Dependencies

### Backend
```bash
# Create requirements.txt with exact versions
pip freeze > requirements.txt

# Or use pip-tools
pip install pip-tools
pip-compile requirements.in
```

### Frontend
```bash
# package-lock.json is automatically created
# Commit it to version control

# Or use yarn.lock
yarn install
```

---

## 🎯 Recommended Package Versions

For **production stability**, use these tested versions:

### Backend
- Python: 3.11.x (not 3.12 yet, some packages incompatible)
- FastAPI: 0.109.x
- Pydantic AI: 0.0.14+
- Supabase: 2.3.x

### Frontend
- Node.js: 18.x LTS (not 20.x yet for stability)
- Next.js: 14.1.x
- React: 18.2.x
- TypeScript: 5.x

---

## 📚 Documentation Links

### Backend
- [FastAPI Docs](https://fastapi.tiangolo.com/)
- [Pydantic AI Docs](https://ai.pydantic.dev/)
- [Supabase Python Docs](https://supabase.com/docs/reference/python)
- [Groq API Docs](https://console.groq.com/docs)

### Frontend
- [Next.js Docs](https://nextjs.org/docs)
- [React Docs](https://react.dev/)
- [Tailwind CSS Docs](https://tailwindcss.com/docs)
- [Radix UI Docs](https://www.radix-ui.com/)
- [shadcn/ui Docs](https://ui.shadcn.com/)

---

This package reference is complete and tested. All versions are compatible and work together! 🎉
