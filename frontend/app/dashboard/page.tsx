'use client';

import { useEffect, useState } from 'react';
import { useRouter } from 'next/navigation';
import Link from 'next/link';
import {
  Activity,
  Pill,
  Calendar,
  MessageSquare,
  LogOut,
  Plus,
  TrendingUp,
} from 'lucide-react';

export default function DashboardPage() {
  const router = useRouter();
  const [user, setUser] = useState<any>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Check if user is logged in
    const token = localStorage.getItem('token');
    const userData = localStorage.getItem('user');

    if (!token || !userData) {
      router.push('/login');
      return;
    }

    setUser(JSON.parse(userData));
    setLoading(false);
  }, [router]);

  const handleLogout = () => {
    localStorage.removeItem('token');
    localStorage.removeItem('user');
    router.push('/');
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-gray-50 flex items-center justify-center">
        <div className="text-center">
          <Activity className="h-12 w-12 text-blue-600 animate-pulse mx-auto mb-4" />
          <p className="text-gray-600">Loading...</p>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      {/* Header */}
      <header className="bg-white border-b">
        <div className="container mx-auto px-4 py-4">
          <div className="flex justify-between items-center">
            <div className="flex items-center space-x-2">
              <Activity className="h-8 w-8 text-blue-600" />
              <span className="text-2xl font-bold text-gray-900">MediCare AI</span>
            </div>
            <div className="flex items-center space-x-4">
              <span className="text-gray-600">Welcome, {user?.name}!</span>
              <button
                onClick={handleLogout}
                className="flex items-center space-x-2 text-gray-600 hover:text-gray-900"
              >
                <LogOut className="h-5 w-5" />
                <span>Logout</span>
              </button>
            </div>
          </div>
        </div>
      </header>

      {/* Main Content */}
      <main className="container mx-auto px-4 py-8">
        {/* Welcome Section */}
        <div className="bg-gradient-to-r from-blue-600 to-blue-700 rounded-2xl p-8 text-white mb-8">
          <h1 className="text-3xl font-bold mb-2">Welcome back, {user?.name}! 👋</h1>
          <p className="text-blue-100">
            Here's your health overview for today. Stay on top of your wellness journey!
          </p>
        </div>

        {/* Quick Actions */}
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-6 mb-8">
          <QuickActionCard
            icon={<Pill className="h-8 w-8" />}
            title="Medications"
            description="View and manage"
            href="/dashboard/medications"
            color="blue"
          />
          <QuickActionCard
            icon={<Calendar className="h-8 w-8" />}
            title="Appointments"
            description="Schedule & view"
            href="/dashboard/appointments"
            color="green"
          />
          <QuickActionCard
            icon={<TrendingUp className="h-8 w-8" />}
            title="Health Metrics"
            description="Track vitals"
            href="/dashboard/health-metrics"
            color="purple"
          />
          <QuickActionCard
            icon={<MessageSquare className="h-8 w-8" />}
            title="AI Assistant"
            description="Chat now"
            href="/dashboard/chat"
            color="orange"
          />
        </div>

        {/* Overview Cards */}
        <div className="grid md:grid-cols-3 gap-6">
          {/* Medications Overview */}
          <div className="bg-white rounded-xl shadow-sm p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-900">Active Medications</h3>
              <Pill className="h-6 w-6 text-blue-600" />
            </div>
            <p className="text-3xl font-bold text-gray-900 mb-2">0</p>
            <p className="text-sm text-gray-600">medications tracked</p>
            <Link
              href="/dashboard/medications"
              className="mt-4 inline-flex items-center text-blue-600 hover:text-blue-700 text-sm font-medium"
            >
              View all
              <Plus className="ml-1 h-4 w-4" />
            </Link>
          </div>

          {/* Appointments Overview */}
          <div className="bg-white rounded-xl shadow-sm p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-900">Upcoming Appointments</h3>
              <Calendar className="h-6 w-6 text-green-600" />
            </div>
            <p className="text-3xl font-bold text-gray-900 mb-2">0</p>
            <p className="text-sm text-gray-600">appointments scheduled</p>
            <Link
              href="/dashboard/appointments"
              className="mt-4 inline-flex items-center text-green-600 hover:text-green-700 text-sm font-medium"
            >
              View all
              <Plus className="ml-1 h-4 w-4" />
            </Link>
          </div>

          {/* Health Metrics Overview */}
          <div className="bg-white rounded-xl shadow-sm p-6">
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-gray-900">Health Metrics</h3>
              <TrendingUp className="h-6 w-6 text-purple-600" />
            </div>
            <p className="text-3xl font-bold text-gray-900 mb-2">0</p>
            <p className="text-sm text-gray-600">metrics logged</p>
            <Link
              href="/dashboard/health-metrics"
              className="mt-4 inline-flex items-center text-purple-600 hover:text-purple-700 text-sm font-medium"
            >
              View all
              <Plus className="ml-1 h-4 w-4" />
            </Link>
          </div>
        </div>

        {/* AI Assistant CTA */}
        <div className="mt-8 bg-gradient-to-r from-orange-500 to-orange-600 rounded-2xl p-8 text-white">
          <div className="flex items-center justify-between">
            <div>
              <h3 className="text-2xl font-bold mb-2">Need Health Guidance?</h3>
              <p className="text-orange-100 mb-4">
                Chat with our AI assistant for personalized health insights and medication reminders.
              </p>
              <Link
                href="/dashboard/chat"
                className="inline-flex items-center bg-white text-orange-600 px-6 py-3 rounded-lg font-semibold hover:bg-orange-50 transition"
              >
                <MessageSquare className="mr-2 h-5 w-5" />
                Start Chatting
              </Link>
            </div>
            <MessageSquare className="h-24 w-24 text-orange-300 hidden lg:block" />
          </div>
        </div>
      </main>
    </div>
  );
}

function QuickActionCard({
  icon,
  title,
  description,
  href,
  color,
}: {
  icon: React.ReactNode;
  title: string;
  description: string;
  href: string;
  color: string;
}) {
  const colorClasses = {
    blue: 'bg-blue-50 text-blue-600 hover:bg-blue-100',
    green: 'bg-green-50 text-green-600 hover:bg-green-100',
    purple: 'bg-purple-50 text-purple-600 hover:bg-purple-100',
    orange: 'bg-orange-50 text-orange-600 hover:bg-orange-100',
  };

  return (
    <Link
      href={href}
      className={`${colorClasses[color as keyof typeof colorClasses]} rounded-xl p-6 transition hover:shadow-md`}
    >
      <div className="mb-3">{icon}</div>
      <h3 className="text-lg font-semibold mb-1">{title}</h3>
      <p className="text-sm opacity-80">{description}</p>
    </Link>
  );
}
