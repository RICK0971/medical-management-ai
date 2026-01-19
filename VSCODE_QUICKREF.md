# 💻 VS Code Quick Reference

Essential shortcuts and commands for developing Medical Management AI.

## ⌨️ Essential Shortcuts

### General
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Command Palette | `Ctrl+Shift+P` | `Cmd+Shift+P` |
| Quick Open File | `Ctrl+P` | `Cmd+P` |
| Settings | `Ctrl+,` | `Cmd+,` |
| Keyboard Shortcuts | `Ctrl+K Ctrl+S` | `Cmd+K Cmd+S` |

### Terminal
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Toggle Terminal | `` Ctrl+` `` | `` Cmd+` `` |
| New Terminal | `` Ctrl+Shift+` `` | `` Cmd+Shift+` `` |
| Split Terminal | `Ctrl+Shift+5` | `Cmd+Shift+5` |
| Kill Terminal | `Ctrl+Shift+K` | `Cmd+Shift+K` |

### Editing
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Format Document | `Shift+Alt+F` | `Shift+Option+F` |
| Go to Line | `Ctrl+G` | `Cmd+G` |
| Delete Line | `Ctrl+Shift+K` | `Cmd+Shift+K` |
| Move Line Up/Down | `Alt+Up/Down` | `Option+Up/Down` |
| Copy Line Up/Down | `Shift+Alt+Up/Down` | `Shift+Option+Up/Down` |
| Multi-cursor | `Alt+Click` | `Option+Click` |
| Select Next Occurrence | `Ctrl+D` | `Cmd+D` |

### Navigation
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Go to Definition | `F12` | `F12` |
| Peek Definition | `Alt+F12` | `Option+F12` |
| Find References | `Shift+F12` | `Shift+F12` |
| Go Back | `Alt+Left` | `Ctrl+-` |
| Go Forward | `Alt+Right` | `Ctrl+Shift+-` |

### Search
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Find | `Ctrl+F` | `Cmd+F` |
| Replace | `Ctrl+H` | `Cmd+H` |
| Find in Files | `Ctrl+Shift+F` | `Cmd+Shift+F` |
| Replace in Files | `Ctrl+Shift+H` | `Cmd+Shift+H` |

### Git
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Source Control | `Ctrl+Shift+G` | `Cmd+Shift+G` |
| Commit | `Ctrl+Enter` | `Cmd+Enter` |

### Debug
| Action | Windows/Linux | macOS |
|--------|--------------|-------|
| Start/Continue | `F5` | `F5` |
| Step Over | `F10` | `F10` |
| Step Into | `F11` | `F11` |
| Step Out | `Shift+F11` | `Shift+F11` |
| Stop | `Shift+F5` | `Shift+F5` |
| Toggle Breakpoint | `F9` | `F9` |

---

## 🚀 Quick Commands

### Python

**Select Interpreter:**
```
Ctrl+Shift+P → Python: Select Interpreter
```

**Run File:**
```
F5 or Click ▶️
```

**Format Code:**
```
Shift+Alt+F
```

### TypeScript/JavaScript

**Restart TS Server:**
```
Ctrl+Shift+P → TypeScript: Restart TS Server
```

**Organize Imports:**
```
Shift+Alt+O
```

### Git

**Stage All:**
```
Ctrl+Shift+G → Click + next to Changes
```

**Commit:**
```
Write message → Ctrl+Enter
```

---

## 📁 Project Structure Navigation

```
Ctrl+P → Type filename → Enter
```

**Quick access:**
- `main.py` - Backend entry
- `page.tsx` - Frontend pages
- `.env` - Environment variables
- `schema.sql` - Database schema

---

## 🐛 Debugging Setup

### Backend (FastAPI)
1. Set breakpoint (click left of line number)
2. Press `F5`
3. Choose "Python: FastAPI"

### Frontend (Next.js)
1. Set breakpoint
2. Press `F5`
3. Choose "Next.js: debug"

---

## 🔧 Common Tasks

### Start Development

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

### Install Packages

**Backend:**
```bash
pip install package-name
pip freeze > requirements.txt
```

**Frontend:**
```bash
npm install package-name
```

### Format All Files

**Python:**
```
Ctrl+Shift+P → Format Document
```

**JavaScript/TypeScript:**
```
Ctrl+Shift+P → Format Document
```

---

## 🎨 Customization

### Change Theme
```
Ctrl+K Ctrl+T
```

### Change Font Size
```
Ctrl+, → Search "font size"
```

### Enable Auto Save
```
File → Auto Save
```

---

## 🔍 Search & Replace

### Find in Current File
```
Ctrl+F
```

### Find in All Files
```
Ctrl+Shift+F
```

### Replace in Current File
```
Ctrl+H
```

### Replace in All Files
```
Ctrl+Shift+H
```

---

## 📦 Extensions Quick Install

```
Ctrl+Shift+X
```

**Search and install:**
- Python
- Pylance
- ESLint
- Prettier
- Tailwind CSS IntelliSense
- GitLens
- Thunder Client

---

## 🎯 Productivity Tips

1. **Use Command Palette** - `Ctrl+Shift+P` for everything
2. **Quick Open** - `Ctrl+P` to open files fast
3. **Multi-cursor** - `Alt+Click` to edit multiple places
4. **Split Editor** - `Ctrl+\` for side-by-side
5. **Zen Mode** - `Ctrl+K Z` for focus
6. **Format on Save** - Already enabled in settings
7. **Auto Import** - Type and press `Ctrl+Space`

---

## 🆘 Troubleshooting

### Reload Window
```
Ctrl+Shift+P → Developer: Reload Window
```

### Clear Cache
```
Ctrl+Shift+P → Developer: Clear Editor History
```

### Python Interpreter Issues
```
Ctrl+Shift+P → Python: Select Interpreter
→ Choose ./backend/venv/bin/python
```

### TypeScript Issues
```
Ctrl+Shift+P → TypeScript: Restart TS Server
```

---

## 📚 Learn More

- **VS Code Docs:** [code.visualstudio.com/docs](https://code.visualstudio.com/docs)
- **Python in VS Code:** [code.visualstudio.com/docs/python](https://code.visualstudio.com/docs/python)
- **Full Guide:** [VSCODE_GUIDE.md](VSCODE_GUIDE.md)

---

**Print this and keep it handy! 📄**
