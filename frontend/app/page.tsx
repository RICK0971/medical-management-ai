import Link from "next/link";
import { ArrowRight, Activity, Calendar, Pill, MessageSquare } from "lucide-react";

export default function Home() {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      {/* Header */}
      <header className="container mx-auto px-4 py-6">
        <nav className="flex justify-between items-center">
          <div className="flex items-center space-x-2">
            <Activity className="h-8 w-8 text-blue-600" />
            <span className="text-2xl font-bold text-gray-900">MediCare AI</span>
          </div>
          <div className="space-x-4">
            <Link href="/login" className="text-gray-600 hover:text-gray-900">
              Login
            </Link>
            <Link
              href="/signup"
              className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700 transition"
            >
              Sign Up
            </Link>
          </div>
        </nav>
      </header>

      {/* Hero Section */}
      <section className="container mx-auto px-4 py-20 text-center">
        <h1 className="text-5xl md:text-6xl font-bold text-gray-900 mb-6">
          Your Personal
          <span className="text-blue-600"> Medical Assistant</span>
        </h1>
        <p className="text-xl text-gray-600 mb-8 max-w-2xl mx-auto">
          Manage medications, track health metrics, schedule appointments, and chat with an AI health assistant - all in one place.
        </p>
        <Link
          href="/signup"
          className="inline-flex items-center bg-blue-600 text-white px-8 py-4 rounded-lg text-lg font-semibold hover:bg-blue-700 transition"
        >
          Get Started Free
          <ArrowRight className="ml-2 h-5 w-5" />
        </Link>
      </section>

      {/* Features */}
      <section className="container mx-auto px-4 py-20">
        <h2 className="text-3xl font-bold text-center mb-12">Everything You Need</h2>
        <div className="grid md:grid-cols-2 lg:grid-cols-4 gap-8">
          <FeatureCard
            icon={<Pill className="h-10 w-10 text-blue-600" />}
            title="Medication Tracking"
            description="Never miss a dose. Track all your medications with smart reminders."
          />
          <FeatureCard
            icon={<Calendar className="h-10 w-10 text-blue-600" />}
            title="Appointments"
            description="Schedule and manage all your doctor appointments in one place."
          />
          <FeatureCard
            icon={<Activity className="h-10 w-10 text-blue-600" />}
            title="Health Metrics"
            description="Log and visualize your vitals - BP, sugar, weight, and more."
          />
          <FeatureCard
            icon={<MessageSquare className="h-10 w-10 text-blue-600" />}
            title="AI Assistant"
            description="Chat with an AI health assistant for guidance and insights."
          />
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-gray-50 border-t mt-20">
        <div className="container mx-auto px-4 py-8 text-center text-gray-600">
          <p className="mb-2">© 2024 Medical Management AI. All rights reserved.</p>
          <p className="text-sm">
            ⚠️ This application is for educational purposes only and should not replace professional medical advice.
          </p>
        </div>
      </footer>
    </div>
  );
}

function FeatureCard({ icon, title, description }: { icon: React.ReactNode; title: string; description: string }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-sm hover:shadow-md transition">
      <div className="mb-4">{icon}</div>
      <h3 className="text-xl font-semibold mb-2">{title}</h3>
      <p className="text-gray-600">{description}</p>
    </div>
  );
}
