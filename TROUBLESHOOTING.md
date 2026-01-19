# 🔧 Troubleshooting Guide

Common issues and solutions for the Medical Management AI project.

## 📋 Table of Contents

- [Backend Issues](#backend-issues)
- [Frontend Issues](#frontend-issues)
- [Database Issues](#database-issues)
- [API Issues](#api-issues)
- [Deployment Issues](#deployment-issues)
- [General Issues](#general-issues)

---

## 🐍 Backend Issues

### Issue: `python: command not found`

**Symptoms:**
```bash
$ python --version
python: command not found
```

**Solutions:**

**Option 1:** Try `python3`
```bash
python3 --version
python3 -m venv venv
```

**Option 2:** Add Python to PATH (Windows)
1. Search "Environment Variables" in Windows
2. Edit "Path" variable
3. Add Python installation directory
4. Restart terminal

**Option 3:** Reinstall Python
- Download from [python.org](https://www.python.org/downloads/)
- ✅ Check "Add Python to PATH" during installation

---

### Issue: `pip: command not found`

**Symptoms:**
```bash
$ pip install -r requirements.txt
pip: command not found
```

**Solutions:**

**Option 1:** Use `python -m pip`
```bash
python -m pip install -r requirements.txt
```

**Option 2:** Install pip
```bash
# macOS/Linux
sudo apt-get install python3-pip

# Or download get-pip.py
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python get-pip.py
```

---

### Issue: Cannot activate virtual environment (Windows)

**Symptoms:**
```powershell
PS> venv\Scripts\activate
... cannot be loaded because running scripts is disabled...
```

**Solution:**

**Run PowerShell as Administrator:**
```powershell
Set-ExecutionPolicy RemoteSigned
```

Then try again:
```powershell
venv\Scripts\activate
```

---

### Issue: `ModuleNotFoundError: No module named 'pydantic_ai'`

**Symptoms:**
```bash
ModuleNotFoundError: No module named 'pydantic_ai'
```

**Solutions:**

**Check 1:** Is venv activated?
```bash
# You should see (venv) in your terminal
# If not, activate it:
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows
```

**Check 2:** Reinstall packages
```bash
pip install -r requirements.txt
```

**Check 3:** Install specific package
```bash
pip install pydantic-ai==0.0.14
```

---

### Issue: `bcrypt` compilation error

**Symptoms:**
```bash
error: Microsoft Visual C++ 14.0 or greater is required
```

**Solutions:**

**Windows:**
1. Install [Visual C++ Build Tools](https://visualstudio.microsoft.com/visual-cpp-build-tools/)
2. Or install [Visual Studio Community](https://visualstudio.microsoft.com/)
3. Restart terminal
4. Try again: `pip install passlib[bcrypt]`

**macOS:**
```bash
xcode-select --install
```

**Linux:**
```bash
sudo apt-get install build-essential python3-dev
```

---

### Issue: Port 8000 already in use

**Symptoms:**
```bash
ERROR: [Errno 48] Address already in use
```

**Solutions:**

**Option 1:** Kill the process
```bash
# macOS/Linux
lsof -ti:8000 | xargs kill -9

# Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

**Option 2:** Use different port
```bash
uvicorn main:app --reload --port 8001
```

---

### Issue: Supabase connection error

**Symptoms:**
```bash
supabase.exceptions.APIError: Invalid API key
```

**Solutions:**

**Check 1:** Verify credentials in `.env`
```env
SUPABASE_URL=https://xxxxx.supabase.co  # No trailing slash
SUPABASE_KEY=eyJhbGc...                 # No extra spaces
```

**Check 2:** Get fresh credentials
1. Go to Supabase dashboard
2. Settings → API
3. Copy new keys
4. Update `.env`
5. Restart backend

**Check 3:** Check project status
- Make sure Supabase project is active
- Check if you're on free tier limits

---

### Issue: Groq API error

**Symptoms:**
```bash
groq.APIError: Invalid API key
```

**Solutions:**

**Check 1:** Verify API key
```env
GROQ_API_KEY=gsk_xxxxx  # Should start with gsk_
```

**Check 2:** Generate new key
1. Go to [console.groq.com](https://console.groq.com/)
2. API Keys → Create API Key
3. Copy and update `.env`
4. Restart backend

**Check 3:** Check rate limits
- Free tier has limits
- Wait a few minutes
- Try again

---

## 📱 Frontend Issues

### Issue: `npm: command not found`

**Symptoms:**
```bash
$ npm install
npm: command not found
```

**Solution:**

Install Node.js from [nodejs.org](https://nodejs.org/)
- Download LTS version
- Install
- Restart terminal
- Verify: `node --version` and `npm --version`

---

### Issue: `npm install` fails

**Symptoms:**
```bash
npm ERR! code ERESOLVE
npm ERR! ERESOLVE unable to resolve dependency tree
```

**Solutions:**

**Option 1:** Clear cache and retry
```bash
npm cache clean --force
rm -rf node_modules package-lock.json
npm install
```

**Option 2:** Use legacy peer deps
```bash
npm install --legacy-peer-deps
```

**Option 3:** Use different Node version
```bash
# Install nvm (Node Version Manager)
# Then use Node 18
nvm install 18
nvm use 18
npm install
```

---

### Issue: Port 3000 already in use

**Symptoms:**
```bash
Error: listen EADDRINUSE: address already in use :::3000
```

**Solutions:**

**Option 1:** Kill the process
```bash
# macOS/Linux
lsof -ti:3000 | xargs kill -9

# Windows
netstat -ano | findstr :3000
taskkill /PID <PID> /F
```

**Option 2:** Use different port
```bash
PORT=3001 npm run dev
```

---

### Issue: `Module not found` errors

**Symptoms:**
```bash
Module not found: Can't resolve '@/components/ui/button'
```

**Solutions:**

**Check 1:** Reinstall dependencies
```bash
rm -rf node_modules package-lock.json
npm install
```

**Check 2:** Check file paths
- Make sure file exists
- Check import path is correct
- Check file extension (.tsx, .ts, .jsx, .js)

**Check 3:** Check tsconfig.json
```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./*"]
    }
  }
}
```

---

### Issue: API connection fails

**Symptoms:**
```bash
Network Error
AxiosError: Request failed with status code 404
```

**Solutions:**

**Check 1:** Is backend running?
```bash
# Open http://localhost:8000/docs
# Should see API documentation
```

**Check 2:** Check API URL
```env
# frontend/.env.local
NEXT_PUBLIC_API_URL=http://localhost:8000  # No /api/v1
```

**Check 3:** Check CORS
```env
# backend/.env
ALLOWED_ORIGINS=http://localhost:3000  # Match frontend URL
```

---

### Issue: Build fails

**Symptoms:**
```bash
npm run build
Error: Build failed
```

**Solutions:**

**Check 1:** Fix TypeScript errors
```bash
npm run type-check
# Fix all errors shown
```

**Check 2:** Check environment variables
```bash
# Make sure .env.local exists
# And has NEXT_PUBLIC_API_URL
```

**Check 3:** Clear Next.js cache
```bash
rm -rf .next
npm run build
```

---

## 🗄️ Database Issues

### Issue: Database schema not created

**Symptoms:**
```bash
relation "users" does not exist
```

**Solutions:**

**Step 1:** Go to Supabase dashboard
**Step 2:** Click "SQL Editor"
**Step 3:** Copy `database/schema.sql`
**Step 4:** Paste and click "Run"
**Step 5:** Should see "Success. No rows returned"

---

### Issue: RLS policies blocking access

**Symptoms:**
```bash
new row violates row-level security policy
```

**Solutions:**

**Option 1:** Disable RLS temporarily (development only)
```sql
ALTER TABLE users DISABLE ROW LEVEL SECURITY;
ALTER TABLE medications DISABLE ROW LEVEL SECURITY;
-- etc.
```

**Option 2:** Use service_role key
```env
# backend/.env
SUPABASE_KEY=your-service-role-key  # Not anon key
```

**Option 3:** Fix RLS policies
- Check policies in Supabase dashboard
- Make sure they match your auth setup

---

### Issue: Database connection timeout

**Symptoms:**
```bash
asyncpg.exceptions.ConnectionDoesNotExistError
```

**Solutions:**

**Check 1:** Verify DATABASE_URL
```env
DATABASE_URL=postgresql://user:pass@host:5432/db
```

**Check 2:** Check Supabase project status
- Go to Supabase dashboard
- Make sure project is active
- Check if paused (free tier)

**Check 3:** Check network
- Try accessing Supabase dashboard
- Check firewall settings
- Try different network

---

## 🔌 API Issues

### Issue: 401 Unauthorized

**Symptoms:**
```json
{
  "detail": "Could not validate credentials"
}
```

**Solutions:**

**Check 1:** Is token valid?
```javascript
// Check localStorage
console.log(localStorage.getItem('token'));
```

**Check 2:** Is token expired?
- Tokens expire after 30 minutes
- Login again to get new token

**Check 3:** Is Authorization header correct?
```javascript
headers: {
  'Authorization': `Bearer ${token}`  // Note the space after Bearer
}
```

---

### Issue: 404 Not Found

**Symptoms:**
```json
{
  "detail": "Not Found"
}
```

**Solutions:**

**Check 1:** Verify endpoint URL
```javascript
// Correct
http://localhost:8000/api/v1/medications

// Wrong
http://localhost:8000/medications
```

**Check 2:** Check API documentation
- Open `http://localhost:8000/docs`
- Verify endpoint exists
- Check HTTP method (GET, POST, etc.)

---

### Issue: 422 Validation Error

**Symptoms:**
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "field required"
    }
  ]
}
```

**Solutions:**

**Check request body:**
```javascript
// Make sure all required fields are included
{
  "email": "user@example.com",  // Required
  "name": "John Doe",           // Required
  "password": "password123"     // Required
}
```

---

### Issue: 500 Internal Server Error

**Symptoms:**
```json
{
  "detail": "Internal server error"
}
```

**Solutions:**

**Check 1:** Look at backend logs
```bash
# Terminal running uvicorn
# Look for error traceback
```

**Check 2:** Check database connection
- Verify Supabase credentials
- Check database is accessible

**Check 3:** Check environment variables
- Make sure all required vars are set
- No typos in variable names

---

## 🚀 Deployment Issues

### Issue: Railway build fails

**Symptoms:**
```
Build failed: pip install error
```

**Solutions:**

**Check 1:** Verify requirements.txt
- Make sure file exists in backend/
- Check for typos
- Verify all packages are available on PyPI

**Check 2:** Check Python version
- Railway uses Python 3.11 by default
- Make sure packages are compatible

**Check 3:** Add runtime.txt
```
# backend/runtime.txt
python-3.11.0
```

---

### Issue: Vercel build fails

**Symptoms:**
```
Build failed: Module not found
```

**Solutions:**

**Check 1:** Verify package.json
- Make sure all dependencies are listed
- Run `npm install` locally first

**Check 2:** Check build command
```json
{
  "scripts": {
    "build": "next build"
  }
}
```

**Check 3:** Check environment variables
- Add `NEXT_PUBLIC_API_URL` in Vercel dashboard
- Redeploy

---

### Issue: CORS errors in production

**Symptoms:**
```
Access to fetch blocked by CORS policy
```

**Solutions:**

**Update backend ALLOWED_ORIGINS:**
```env
# Railway environment variables
ALLOWED_ORIGINS=https://your-app.vercel.app
```

**Redeploy backend**

---

## 🔍 General Issues

### Issue: Changes not reflecting

**Solutions:**

**Backend:**
```bash
# Make sure --reload is enabled
uvicorn main:app --reload

# Or restart server
Ctrl+C
uvicorn main:app --reload
```

**Frontend:**
```bash
# Next.js auto-reloads
# If not, restart:
Ctrl+C
npm run dev
```

---

### Issue: Slow performance

**Solutions:**

**Backend:**
- Check database queries
- Add indexes to frequently queried columns
- Enable caching

**Frontend:**
- Check Network tab in browser DevTools
- Optimize images
- Use React.memo for expensive components

---

### Issue: Memory errors

**Symptoms:**
```bash
JavaScript heap out of memory
```

**Solutions:**

**Increase Node memory:**
```bash
NODE_OPTIONS=--max_old_space_size=4096 npm run dev
```

**Or in package.json:**
```json
{
  "scripts": {
    "dev": "NODE_OPTIONS='--max_old_space_size=4096' next dev"
  }
}
```

---

## 🆘 Still Having Issues?

### Debug Checklist

- [ ] Check all environment variables
- [ ] Verify all services are running
- [ ] Check terminal for error messages
- [ ] Check browser console (F12)
- [ ] Check API documentation (`/docs`)
- [ ] Review logs in Supabase dashboard
- [ ] Try restarting everything
- [ ] Clear cache and reinstall packages

### Get Help

1. **Check Documentation:**
   - [INSTALLATION.md](INSTALLATION.md)
   - [QUICKSTART.md](QUICKSTART.md)
   - [docs/SETUP.md](docs/SETUP.md)

2. **Search Issues:**
   - Check GitHub issues
   - Search Stack Overflow
   - Check package documentation

3. **Ask for Help:**
   - Open GitHub issue
   - Include error messages
   - Include steps to reproduce
   - Include environment details

---

## 📝 Reporting Bugs

When reporting issues, include:

```
**Environment:**
- OS: [e.g., Windows 11, macOS 14, Ubuntu 22.04]
- Python version: [e.g., 3.11.5]
- Node version: [e.g., 18.17.0]
- Browser: [e.g., Chrome 120]

**Steps to Reproduce:**
1. Go to '...'
2. Click on '...'
3. See error

**Expected Behavior:**
What you expected to happen

**Actual Behavior:**
What actually happened

**Error Messages:**
```
Paste error messages here
```

**Screenshots:**
If applicable, add screenshots
```

---

**Most issues can be solved by:**
1. ✅ Checking environment variables
2. ✅ Restarting servers
3. ✅ Clearing cache and reinstalling
4. ✅ Reading error messages carefully
5. ✅ Checking the documentation

Good luck! 🍀
