'use client';

import { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  Activity,
  TrendingUp,
  Plus,
  Trash2,
  Calendar,
  ArrowLeft,
  AlertCircle,
  Heart,
  Droplet,
  Weight,
  Thermometer,
} from 'lucide-react';
import axios from 'axios';

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

interface HealthMetric {
  id: string;
  metric_type: string;
  value: number;
  unit: string;
  recorded_at: string;
  notes?: string;
}

const metricTypes = [
  { value: 'blood_pressure', label: 'Blood Pressure', icon: Heart, unit: 'mmHg' },
  { value: 'blood_sugar', label: 'Blood Sugar', icon: Droplet, unit: 'mg/dL' },
  { value: 'weight', label: 'Weight', icon: Weight, unit: 'kg' },
  { value: 'temperature', label: 'Temperature', icon: Thermometer, unit: '°F' },
  { value: 'heart_rate', label: 'Heart Rate', icon: Activity, unit: 'bpm' },
];

export default function HealthMetricsPage() {
  const router = useRouter();
  const [metrics, setMetrics] = useState<HealthMetric[]>([]);
  const [loading, setLoading] = useState(true);
  const [showAddForm, setShowAddForm] = useState(false);
  const [error, setError] = useState('');
  const [formData, setFormData] = useState({
    metric_type: 'blood_pressure',
    value: '',
    unit: 'mmHg',
    notes: '',
  });

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (!token) {
      router.push('/login');
      return;
    }
    fetchMetrics();
  }, [router]);

  const fetchMetrics = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await axios.get(`${API_URL}/api/v1/health-metrics/`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      setMetrics(response.data);
    } catch (err: any) {
      setError('Failed to load health metrics');
      console.error(err);
    } finally {
      setLoading(false);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setError('');

    try {
      const token = localStorage.getItem('token');
      await axios.post(
        `${API_URL}/api/v1/health-metrics/`,
        {
          ...formData,
          value: parseFloat(formData.value),
        },
        {
          headers: { Authorization: `Bearer ${token}` },
        }
      );

      setShowAddForm(false);
      setFormData({
        metric_type: 'blood_pressure',
        value: '',
        unit: 'mmHg',
        notes: '',
      });
      fetchMetrics();
    } catch (err: any) {
      setError(err.response?.data?.detail || 'Failed to add health metric');
    }
  };

  const handleDelete = async (id: string) => {
    if (!confirm('Are you sure you want to delete this metric?')) return;

    try {
      const token = localStorage.getItem('token');
      await axios.delete(`${API_URL}/api/v1/health-metrics/${id}`, {
        headers: { Authorization: `Bearer ${token}` },
      });
      fetchMetrics();
    } catch (err: any) {
      setError('Failed to delete metric');
    }
  };

  const handleMetricTypeChange = (type: string) => {
    const metric = metricTypes.find((m) => m.value === type);
    setFormData({
      ...formData,
      metric_type: type,
      unit: metric?.unit || '',
    });
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <Activity className="h-12 w-12 text-blue-600 animate-pulse" />
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b">
        <div className="container mx-auto px-4 py-4">
          <div className="flex items-center justify-between">
            <div className="flex items-center space-x-4">
              <Link href="/dashboard" className="text-gray-600 hover:text-gray-900">
                <ArrowLeft className="h-6 w-6" />
              </Link>
              <div className="flex items-center space-x-2">
                <TrendingUp className="h-8 w-8 text-purple-600" />
                <h1 className="text-2xl font-bold text-gray-900">Health Metrics</h1>
              </div>
            </div>
            <button
              onClick={() => setShowAddForm(true)}
              className="flex items-center space-x-2 bg-purple-600 text-white px-4 py-2 rounded-lg hover:bg-purple-700"
            >
              <Plus className="h-5 w-5" />
              <span>Log Metric</span>
            </button>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {error && (
          <div className="mb-6 bg-red-50 border border-red-200 rounded-lg p-4 flex items-start space-x-3">
            <AlertCircle className="h-5 w-5 text-red-600 mt-0.5" />
            <p className="text-sm text-red-600">{error}</p>
          </div>
        )}

        {/* Add Metric Form */}
        {showAddForm && (
          <div className="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center p-4 z-50">
            <div className="bg-white rounded-2xl p-8 max-w-md w-full">
              <h2 className="text-2xl font-bold mb-6">Log Health Metric</h2>
              <form onSubmit={handleSubmit} className="space-y-4">
                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Metric Type
                  </label>
                  <select
                    value={formData.metric_type}
                    onChange={(e) => handleMetricTypeChange(e.target.value)}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500"
                  >
                    {metricTypes.map((type) => (
                      <option key={type.value} value={type.value}>
                        {type.label}
                      </option>
                    ))}
                  </select>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Value
                  </label>
                  <div className="flex space-x-2">
                    <input
                      type="number"
                      step="0.1"
                      value={formData.value}
                      onChange={(e) => setFormData({ ...formData, value: e.target.value })}
                      className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500"
                      required
                    />
                    <input
                      type="text"
                      value={formData.unit}
                      readOnly
                      className="w-24 px-4 py-2 border border-gray-300 rounded-lg bg-gray-50"
                    />
                  </div>
                </div>

                <div>
                  <label className="block text-sm font-medium text-gray-700 mb-2">
                    Notes (Optional)
                  </label>
                  <textarea
                    value={formData.notes}
                    onChange={(e) => setFormData({ ...formData, notes: e.target.value })}
                    className="w-full px-4 py-2 border border-gray-300 rounded-lg focus:ring-2 focus:ring-purple-500"
                    rows={3}
                  />
                </div>

                <div className="flex space-x-3 pt-4">
                  <button
                    type="submit"
                    className="flex-1 bg-purple-600 text-white py-2 rounded-lg hover:bg-purple-700"
                  >
                    Log Metric
                  </button>
                  <button
                    type="button"
                    onClick={() => setShowAddForm(false)}
                    className="flex-1 bg-gray-200 text-gray-700 py-2 rounded-lg hover:bg-gray-300"
                  >
                    Cancel
                  </button>
                </div>
              </form>
            </div>
          </div>
        )}

        {/* Metrics List */}
        {metrics.length === 0 ? (
          <div className="text-center py-12">
            <TrendingUp className="h-16 w-16 text-gray-300 mx-auto mb-4" />
            <h3 className="text-xl font-semibold text-gray-600 mb-2">No metrics logged yet</h3>
            <p className="text-gray-500 mb-6">Start tracking your health vitals</p>
            <button
              onClick={() => setShowAddForm(true)}
              className="bg-purple-600 text-white px-6 py-3 rounded-lg hover:bg-purple-700"
            >
              Log Your First Metric
            </button>
          </div>
        ) : (
          <div className="space-y-4">
            {metrics.map((metric) => {
              const metricType = metricTypes.find((m) => m.value === metric.metric_type);
              const Icon = metricType?.icon || Activity;

              return (
                <div key={metric.id} className="bg-white rounded-xl shadow-sm p-6 hover:shadow-md transition">
                  <div className="flex items-start justify-between">
                    <div className="flex items-center space-x-4 flex-1">
                      <div className="bg-purple-100 p-3 rounded-lg">
                        <Icon className="h-6 w-6 text-purple-600" />
                      </div>
                      <div className="flex-1">
                        <h3 className="font-semibold text-gray-900">
                          {metricType?.label || metric.metric_type}
                        </h3>
                        <p className="text-2xl font-bold text-purple-600 mt-1">
                          {metric.value} {metric.unit}
                        </p>
                        <div className="flex items-center text-sm text-gray-600 mt-2">
                          <Calendar className="h-4 w-4 mr-2" />
                          <span>{new Date(metric.recorded_at).toLocaleString()}</span>
                        </div>
                        {metric.notes && (
                          <p className="text-gray-600 mt-3 text-sm">{metric.notes}</p>
                        )}
                      </div>
                    </div>

                    <button
                      onClick={() => handleDelete(metric.id)}
                      className="text-red-600 hover:text-red-700 ml-4"
                    >
                      <Trash2 className="h-5 w-5" />
                    </button>
                  </div>
                </div>
              );
            })}
          </div>
        )}
      </main>
    </div>
  );
}
