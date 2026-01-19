import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

// Create axios instance
const api = axios.create({
  baseURL: `${API_URL}/api/v1`,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Add auth token to requests
api.interceptors.request.use((config) => {
  const token = localStorage.getItem('token');
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth API
export const authAPI = {
  signup: (data: { email: string; name: string; password: string }) =>
    api.post('/auth/signup', data),
  login: (data: { email: string; password: string }) =>
    api.post('/auth/login', data),
};

// Medications API
export const medicationsAPI = {
  getAll: (activeOnly = true) =>
    api.get('/medications', { params: { active_only: activeOnly } }),
  create: (data: any) => api.post('/medications', data),
  update: (id: string, data: any) => api.patch(`/medications/${id}`, data),
  delete: (id: string) => api.delete(`/medications/${id}`),
};

// Appointments API
export const appointmentsAPI = {
  getAll: () => api.get('/appointments'),
  create: (data: any) => api.post('/appointments', data),
  update: (id: string, data: any) => api.patch(`/appointments/${id}`, data),
  delete: (id: string) => api.delete(`/appointments/${id}`),
};

// Health Metrics API
export const healthMetricsAPI = {
  getAll: (metricType?: string) =>
    api.get('/health-metrics', { params: { metric_type: metricType } }),
  create: (data: any) => api.post('/health-metrics', data),
  delete: (id: string) => api.delete(`/health-metrics/${id}`),
};

// Chat API
export const chatAPI = {
  sendMessage: (message: string) => api.post('/chat', { message }),
};

export default api;
