# 💻 VS Code Developer Guide

Complete guide to developing the Medical Management AI project in Visual Studio Code.

## 📦 Initial Setup

### 1. Clone and Open Project

```bash
git clone https://github.com/RICK0971/medical-management-ai.git
cd medical-management-ai
code .
```

### 2. Install Recommended Extensions

When you open the project, VS Code will prompt:
> "This workspace has extension recommendations."

Click **"Install All"** or install manually:

**Required:**
- `ms-python.python` - Python
- `ms-python.vscode-pylance` - Pylance
- `dbaeumer.vscode-eslint` - ESLint
- `esbenp.prettier-vscode` - Prettier

**Recommended:**
- `bradlc.vscode-tailwindcss` - Tailwind CSS IntelliSense
- `eamodio.gitlens` - GitLens
- `rangav.vscode-thunder-client` - Thunder Client (API testing)
- `usernamehw.errorlens` - Error Lens

### 3. Configure Python Interpreter

1. Press `Ctrl+Shift+P`
2. Type "Python: Select Interpreter"
3. Choose `./backend/venv/bin/python`

---

## 🎯 Workspace Configuration

The project includes `.vscode/` folder with:

### settings.json
Workspace-specific settings:
- Python interpreter path
- Auto-formatting on save
- Linting configuration
- File exclusions
- Tailwind IntelliSense

### extensions.json
Recommended extensions list that VS Code will prompt you to install.

### launch.json
Debug configurations:
- **Python: FastAPI** - Debug backend
- **Next.js: debug** - Debug frontend

---

## 🔧 Terminal Management

### Open Terminal
- Press `` Ctrl+` `` (backtick)
- Or: View → Terminal
- Or: Terminal → New Terminal

### Split Terminal
1. Click terminal panel
2. Click split icon (⊞) in top-right
3. Now you can run backend and frontend side-by-side

### Multiple Terminals
- Click `+` icon to create new terminal
- Use dropdown to switch between terminals
- Name terminals: Right-click → Rename

### Recommended Setup
```
Terminal 1: Backend (Python)
├── cd backend
├── source venv/bin/activate
└── uvicorn main:app --reload

Terminal 2: Frontend (Node.js)
├── cd frontend
└── npm run dev
```

---

## 🐍 Python Development

### Select Interpreter
```
Ctrl+Shift+P → Python: Select Interpreter
→ Choose ./backend/venv/bin/python
```

### Run Python File
- Click ▶️ button in top-right
- Or press `F5`
- Or right-click → Run Python File

### Debugging Python

**Set Breakpoints:**
1. Click left of line number (red dot appears)
2. Press `F5`
3. Choose "Python: FastAPI"

**Debug Controls:**
- `F5` - Continue
- `F10` - Step Over
- `F11` - Step Into
- `Shift+F11` - Step Out
- `Shift+F5` - Stop

**Debug Console:**
- View variables
- Evaluate expressions
- Execute code

### Linting & Formatting

**Auto-format on save:**
Already configured in `.vscode/settings.json`

**Manual format:**
- `Shift+Alt+F` (Windows/Linux)
- `Shift+Option+F` (Mac)

**Organize imports:**
- `Shift+Alt+O` (Windows/Linux)
- `Shift+Option+O` (Mac)

### Python IntelliSense

**Auto-complete:**
- Start typing
- Press `Ctrl+Space` for suggestions

**Go to Definition:**
- `F12` or `Ctrl+Click`

**Peek Definition:**
- `Alt+F12`

**Find All References:**
- `Shift+F12`

---

## 📱 JavaScript/TypeScript Development

### TypeScript Version

**Select TypeScript version:**
```
Ctrl+Shift+P → TypeScript: Select TypeScript Version
→ Use Workspace Version
```

### Formatting

**Auto-format on save:**
Already configured for `.js`, `.ts`, `.tsx` files

**Manual format:**
- `Shift+Alt+F`

### ESLint

**Fix all auto-fixable problems:**
```
Ctrl+Shift+P → ESLint: Fix all auto-fixable Problems
```

### React/Next.js Features

**Component snippets:**
Type `rafce` → React Arrow Function Component Export

**Import auto-complete:**
- Type component name
- Press `Ctrl+Space`
- Select from suggestions
- Import added automatically

**Rename symbol:**
- `F2` on component/variable
- Renames everywhere

---

## 🎨 Tailwind CSS

### IntelliSense

**Auto-complete classes:**
```tsx
<div className="flex |">
              ↑ cursor here, press Ctrl+Space
```

**Class suggestions:**
- Hover over class for CSS preview
- `Ctrl+Click` to see definition

### Class Sorting

**Sort Tailwind classes:**
```
Ctrl+Shift+P → Tailwind CSS: Sort Classes
```

---

## 🐛 Debugging

### Backend (FastAPI)

**Start debugging:**
1. Press `F5`
2. Choose "Python: FastAPI"
3. Backend starts in debug mode

**Set breakpoints:**
- Click left of line number
- Conditional breakpoints: Right-click → Add Conditional Breakpoint

**Debug features:**
- Watch variables
- Call stack
- Breakpoints panel
- Debug console

### Frontend (Next.js)

**Debug server-side:**
1. Press `F5`
2. Choose "Next.js: debug server-side"

**Debug client-side:**
1. Press `F5`
2. Choose "Next.js: debug client-side"
3. Chrome opens with debugger attached

**Debug full stack:**
1. Press `F5`
2. Choose "Next.js: debug full stack"

---

## 🔍 Search & Navigation

### Quick Open
- `Ctrl+P` - Open file by name
- `Ctrl+Shift+P` - Command palette
- `Ctrl+Shift+O` - Go to symbol in file
- `Ctrl+T` - Go to symbol in workspace

### Search
- `Ctrl+F` - Find in file
- `Ctrl+H` - Replace in file
- `Ctrl+Shift+F` - Find in all files
- `Ctrl+Shift+H` - Replace in all files

### Navigation
- `Ctrl+G` - Go to line
- `Alt+Left/Right` - Navigate back/forward
- `Ctrl+Tab` - Switch between open files

---

## 📝 Editing

### Multi-cursor
- `Alt+Click` - Add cursor
- `Ctrl+Alt+Up/Down` - Add cursor above/below
- `Ctrl+D` - Select next occurrence
- `Ctrl+Shift+L` - Select all occurrences

### Line Operations
- `Ctrl+X` - Cut line
- `Ctrl+C` - Copy line
- `Alt+Up/Down` - Move line up/down
- `Shift+Alt+Up/Down` - Copy line up/down
- `Ctrl+Shift+K` - Delete line

### Code Folding
- `Ctrl+Shift+[` - Fold
- `Ctrl+Shift+]` - Unfold
- `Ctrl+K Ctrl+0` - Fold all
- `Ctrl+K Ctrl+J` - Unfold all

---

## 🧪 Testing

### Python Tests

**Run tests:**
```bash
# In terminal
cd backend
pytest tests/ -v
```

**Test Explorer:**
1. Install Python Test Explorer extension
2. Click Testing icon in sidebar
3. Run/debug tests from UI

### Frontend Tests

**Run tests:**
```bash
# In terminal
cd frontend
npm test
```

---

## 🔌 API Testing with Thunder Client

### Install Extension
```
Ctrl+Shift+X → Search "Thunder Client" → Install
```

### Create Request
1. Click Thunder Client icon in sidebar
2. Click "New Request"
3. Set method (GET, POST, etc.)
4. Enter URL: `http://localhost:8000/api/v1/...`
5. Add headers, body, etc.
6. Click "Send"

### Save Collections
- Save requests in collections
- Export/import collections
- Environment variables

---

## 📊 Git Integration

### Source Control Panel
- Click Source Control icon (left sidebar)
- Or press `Ctrl+Shift+G`

### Common Operations

**Stage changes:**
- Click `+` next to file
- Or `+` next to "Changes" to stage all

**Commit:**
1. Write commit message
2. Click ✓ or press `Ctrl+Enter`

**Push/Pull:**
- Click `...` → Push/Pull

**View diff:**
- Click file in Source Control panel
- See side-by-side diff

### GitLens Features

**Blame annotations:**
- Shows who changed each line
- Hover for commit details

**File history:**
- Right-click file → GitLens → View File History

**Compare branches:**
- Click GitLens icon → Compare

---

## ⚙️ Customization

### User Settings

**Open settings:**
- `Ctrl+,` or File → Preferences → Settings

**Common settings:**
```json
{
  "editor.fontSize": 14,
  "editor.tabSize": 2,
  "editor.wordWrap": "on",
  "terminal.integrated.fontSize": 13,
  "workbench.colorTheme": "Dark+ (default dark)"
}
```

### Keyboard Shortcuts

**Open shortcuts:**
- `Ctrl+K Ctrl+S` or File → Preferences → Keyboard Shortcuts

**Customize:**
- Search for command
- Click pencil icon
- Press new key combination

---

## 🎨 Themes & Icons

### Color Themes
```
Ctrl+K Ctrl+T → Choose theme
```

**Popular themes:**
- Dark+ (default)
- One Dark Pro
- Dracula
- Material Theme

### File Icons
```
Ctrl+Shift+P → Preferences: File Icon Theme
```

**Popular icon themes:**
- Material Icon Theme
- VSCode Icons

---

## 🚀 Productivity Tips

### Snippets

**Create custom snippet:**
1. `Ctrl+Shift+P` → Preferences: Configure User Snippets
2. Choose language
3. Add snippet:

```json
{
  "FastAPI Route": {
    "prefix": "route",
    "body": [
      "@router.${1:get}(\"/${2:path}\")",
      "async def ${3:function_name}():",
      "    ${4:pass}"
    ]
  }
}
```

### Emmet

**HTML/JSX shortcuts:**
```
div.container>ul>li*3
→ Tab
→ Expands to full HTML
```

### Zen Mode

**Distraction-free coding:**
- `Ctrl+K Z` - Enter Zen Mode
- `Esc Esc` - Exit Zen Mode

### Split Editor

**Side-by-side editing:**
- `Ctrl+\` - Split editor
- `Ctrl+1/2/3` - Focus editor group

---

## 🔧 Troubleshooting

### Python Issues

**Interpreter not found:**
```
Ctrl+Shift+P → Python: Select Interpreter
→ Enter interpreter path manually
```

**Linting not working:**
```
Ctrl+Shift+P → Python: Enable Linting
```

**Import errors:**
```
Ctrl+Shift+P → Python: Clear Cache and Reload Window
```

### TypeScript Issues

**IntelliSense not working:**
```
Ctrl+Shift+P → TypeScript: Restart TS Server
```

**Wrong TypeScript version:**
```
Ctrl+Shift+P → TypeScript: Select TypeScript Version
→ Use Workspace Version
```

### General Issues

**Reload window:**
```
Ctrl+Shift+P → Developer: Reload Window
```

**Clear cache:**
```
Ctrl+Shift+P → Developer: Clear Editor History
```

---

## 📚 Useful Extensions

### Python Development
- **Python** - Essential
- **Pylance** - IntelliSense
- **Python Indent** - Auto-indentation
- **autoDocstring** - Generate docstrings
- **Python Test Explorer** - Run tests in UI

### Web Development
- **ESLint** - Linting
- **Prettier** - Formatting
- **Auto Rename Tag** - Rename HTML tags
- **Path Intellisense** - Autocomplete paths
- **Import Cost** - Show import sizes
- **Console Ninja** - Better console.log

### General
- **GitLens** - Git supercharged
- **Thunder Client** - API testing
- **Error Lens** - Inline errors
- **Todo Tree** - Track TODOs
- **Better Comments** - Colorful comments
- **Bracket Pair Colorizer** - Colorful brackets
- **Live Share** - Collaborative coding

### Database
- **PostgreSQL** - PostgreSQL support
- **SQLTools** - Database management

---

## 🎯 Workflow Example

### Starting Development

1. **Open VS Code**
   ```bash
   cd medical-management-ai
   code .
   ```

2. **Open terminals** (`` Ctrl+` ``)
   - Split terminal (⊞ icon)
   - Terminal 1: Backend
   - Terminal 2: Frontend

3. **Start backend**
   ```bash
   cd backend
   source venv/bin/activate
   uvicorn main:app --reload
   ```

4. **Start frontend**
   ```bash
   cd frontend
   npm run dev
   ```

5. **Start coding!**
   - Edit files
   - Auto-save enabled
   - Auto-format on save
   - See changes live

### Making Changes

1. **Edit code**
   - Use IntelliSense (`Ctrl+Space`)
   - Format (`Shift+Alt+F`)
   - Save (`Ctrl+S`)

2. **Test changes**
   - Backend: Check terminal logs
   - Frontend: Check browser
   - API: Use Thunder Client

3. **Debug if needed**
   - Set breakpoints
   - Press `F5`
   - Step through code

4. **Commit changes**
   - `Ctrl+Shift+G` - Open Source Control
   - Stage files
   - Write commit message
   - Commit (`Ctrl+Enter`)

---

## 💡 Pro Tips

1. **Learn keyboard shortcuts** - Much faster than mouse
2. **Use Command Palette** - `Ctrl+Shift+P` for everything
3. **Master multi-cursor** - Edit multiple lines at once
4. **Use snippets** - Save time with code templates
5. **Customize settings** - Make VS Code yours
6. **Install extensions** - Enhance functionality
7. **Use Git integration** - No need for separate Git client
8. **Debug, don't print** - Use debugger instead of console.log
9. **Split editor** - View multiple files side-by-side
10. **Use Zen Mode** - Focus when needed

---

**Master VS Code and become a productivity ninja! 🥷**
