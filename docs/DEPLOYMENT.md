# Deployment Guide

Deploy your Medical Management AI application to production.

## Overview

- **Backend**: Railway (or Render)
- **Frontend**: Vercel
- **Database**: Supabase (already cloud-hosted)

## Prerequisites

- GitHub account
- Railway/Render account
- Vercel account
- Supabase project (from setup)

---

## Backend Deployment (Railway)

### Option 1: Railway (Recommended)

**1. Create Railway Account**
- Go to [railway.app](https://railway.app/)
- Sign up with GitHub

**2. Create New Project**
- Click "New Project"
- Select "Deploy from GitHub repo"
- Choose your `medical-management-ai` repository
- Railway will auto-detect the backend

**3. Configure Build Settings**
- Railway should auto-detect Python
- Root directory: `backend`
- Build command: `pip install -r requirements.txt`
- Start command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**4. Add Environment Variables**

Go to Variables tab and add:

```
SUPABASE_URL=https://your-project.supabase.co
SUPABASE_KEY=your-anon-key
SUPABASE_SERVICE_KEY=your-service-key
GROQ_API_KEY=your-groq-key
SECRET_KEY=your-secret-key-min-32-chars
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30
ENVIRONMENT=production
DEBUG=False
ALLOWED_ORIGINS=https://your-frontend-url.vercel.app
```

**5. Deploy**
- Click "Deploy"
- Wait for build to complete
- Copy your Railway URL (e.g., `https://your-app.railway.app`)

### Option 2: Render

**1. Create Render Account**
- Go to [render.com](https://render.com/)
- Sign up with GitHub

**2. Create New Web Service**
- Click "New +" → "Web Service"
- Connect your GitHub repository
- Select `medical-management-ai`

**3. Configure Service**
- Name: `medical-management-backend`
- Root Directory: `backend`
- Environment: `Python 3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `uvicorn main:app --host 0.0.0.0 --port $PORT`

**4. Add Environment Variables**
(Same as Railway above)

**5. Deploy**
- Click "Create Web Service"
- Wait for deployment
- Copy your Render URL

---

## Frontend Deployment (Vercel)

**1. Create Vercel Account**
- Go to [vercel.com](https://vercel.com/)
- Sign up with GitHub

**2. Import Project**
- Click "Add New..." → "Project"
- Import your `medical-management-ai` repository

**3. Configure Project**
- Framework Preset: Next.js
- Root Directory: `frontend`
- Build Command: `npm run build`
- Output Directory: `.next`

**4. Add Environment Variables**

```
NEXT_PUBLIC_API_URL=https://your-backend-url.railway.app
```

**5. Deploy**
- Click "Deploy"
- Wait for build to complete
- Your app will be live at `https://your-app.vercel.app`

**6. Update Backend CORS**

Go back to Railway/Render and update `ALLOWED_ORIGINS`:

```
ALLOWED_ORIGINS=https://your-app.vercel.app
```

Redeploy the backend.

---

## Post-Deployment Steps

### 1. Test the Application

- Visit your Vercel URL
- Sign up for a new account
- Test all features:
  - Add medication
  - Schedule appointment
  - Log health metric
  - Chat with AI

### 2. Set Up Custom Domain (Optional)

**Vercel:**
- Go to Project Settings → Domains
- Add your custom domain
- Follow DNS configuration instructions

**Railway:**
- Go to Settings → Domains
- Add custom domain
- Update DNS records

### 3. Enable HTTPS

Both Vercel and Railway provide automatic HTTPS. Make sure:
- Frontend uses `https://`
- Backend uses `https://`
- Update `NEXT_PUBLIC_API_URL` if needed

### 4. Monitor Logs

**Railway:**
- Go to Deployments → View Logs
- Monitor for errors

**Vercel:**
- Go to Deployments → View Function Logs
- Check for build/runtime errors

**Supabase:**
- Go to Logs → API Logs
- Monitor database queries

---

## Environment Variables Checklist

### Backend (Railway/Render)

- [ ] `SUPABASE_URL`
- [ ] `SUPABASE_KEY`
- [ ] `SUPABASE_SERVICE_KEY`
- [ ] `GROQ_API_KEY`
- [ ] `SECRET_KEY`
- [ ] `ALGORITHM`
- [ ] `ACCESS_TOKEN_EXPIRE_MINUTES`
- [ ] `ENVIRONMENT=production`
- [ ] `DEBUG=False`
- [ ] `ALLOWED_ORIGINS` (with Vercel URL)

### Frontend (Vercel)

- [ ] `NEXT_PUBLIC_API_URL` (Railway/Render URL)

---

## Troubleshooting

### Backend Issues

**Build fails:**
- Check Python version (should be 3.11+)
- Verify `requirements.txt` is correct
- Check Railway/Render logs

**Runtime errors:**
- Check environment variables
- Verify Supabase connection
- Check Groq API key
- Review logs for specific errors

**CORS errors:**
- Update `ALLOWED_ORIGINS` with exact Vercel URL
- Include `https://` protocol
- Redeploy after changes

### Frontend Issues

**Build fails:**
- Check Node version (should be 18+)
- Verify `package.json` dependencies
- Check Vercel build logs

**API connection fails:**
- Verify `NEXT_PUBLIC_API_URL` is correct
- Check backend is running
- Test backend URL directly

**404 errors:**
- Check Next.js routing
- Verify build output
- Check Vercel deployment logs

---

## Performance Optimization

### Backend

1. **Enable caching:**
```python
# Add to main.py
from fastapi_cache import FastAPICache
from fastapi_cache.backends.inmemory import InMemoryBackend

@app.on_event("startup")
async def startup():
    FastAPICache.init(InMemoryBackend())
```

2. **Add rate limiting:**
```python
from slowapi import Limiter
from slowapi.util import get_remote_address

limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter
```

### Frontend

1. **Enable image optimization:**
```javascript
// next.config.js
module.exports = {
  images: {
    domains: ['your-domain.com'],
  },
}
```

2. **Add loading states:**
- Use React Suspense
- Add skeleton loaders
- Implement optimistic updates

---

## Scaling

### Database (Supabase)

- Monitor usage in Supabase dashboard
- Upgrade plan if needed
- Add database indexes for performance

### Backend (Railway/Render)

- Monitor resource usage
- Upgrade instance size if needed
- Consider adding Redis for caching

### Frontend (Vercel)

- Vercel auto-scales
- Monitor bandwidth usage
- Optimize images and assets

---

## Security Checklist

- [ ] HTTPS enabled on all services
- [ ] Environment variables secured
- [ ] CORS properly configured
- [ ] Rate limiting enabled
- [ ] Input validation on all endpoints
- [ ] SQL injection protection (Supabase handles this)
- [ ] XSS protection (React handles this)
- [ ] Strong JWT secret key
- [ ] Password hashing enabled

---

## Monitoring & Maintenance

### Set Up Monitoring

1. **Sentry** (Error tracking)
   - Sign up at sentry.io
   - Add to both frontend and backend
   - Get alerts for errors

2. **Uptime monitoring**
   - Use UptimeRobot or similar
   - Monitor both frontend and backend
   - Get alerts if down

### Regular Maintenance

- [ ] Check logs weekly
- [ ] Monitor API usage
- [ ] Update dependencies monthly
- [ ] Backup database regularly
- [ ] Review security alerts

---

## Cost Estimate

**Free Tier:**
- Supabase: Free (500MB database, 50MB file storage)
- Railway: $5/month credit (enough for small apps)
- Vercel: Free (100GB bandwidth)
- Groq: Free (limited requests)

**Total: ~$0-5/month for small usage**

**Paid Tier (for production):**
- Supabase Pro: $25/month
- Railway: ~$10-20/month
- Vercel Pro: $20/month
- Groq: Pay as you go

**Total: ~$55-65/month**

---

## Next Steps

- Set up custom domain
- Add monitoring
- Enable analytics
- Add more features
- Optimize performance
- Scale as needed

## Support

- Railway: [docs.railway.app](https://docs.railway.app/)
- Vercel: [vercel.com/docs](https://vercel.com/docs)
- Supabase: [supabase.com/docs](https://supabase.com/docs)
