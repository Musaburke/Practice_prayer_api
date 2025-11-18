import React from "react";
import { Link } from "react-router-dom";

const Home = () => {
  return (
    <div
      className="min-h-screen flex flex-col items-center justify-center p-6 bg-cover bg-center"
      style={{ backgroundImage: "url(/images/background1.png)" }}
    >
      {/* Overlay (optional, for better contrast) */}
      <div className="absolute inset-0 bg-black opacity-40"></div>

      {/* Content */}
      <div className="relative z-10 text-center">
        <header className="mb-12">
          <h1 className="text-5xl md:text-6xl font-extrabold mb-4 text-white">
            🌙 Islamic Tools Hub
          </h1>
          <h2 className="text-xl md:text-2xl text-gray-200">
            All your Islamic tools in one place
          </h2>
        </header>

        <div className="grid grid-cols-1 sm:grid-cols-2 gap-6">
          <Link to="/prayer">
            <button className="w-full bg-blue-500 text-white py-3 px-6 rounded-lg shadow hover:bg-blue-600 transition">
              Prayer Times
            </button>
          </Link>
          <Link to="/tasbeeh">
            <button className="w-full bg-green-500 text-white py-3 px-6 rounded-lg shadow hover:bg-green-600 transition">
              Tasbeeh Counter
            </button>
          </Link>
          <Link to="/hadith">
            <button className="w-full bg-purple-500 text-white py-3 px-6 rounded-lg shadow hover:bg-purple-600 transition">
              Random Hadith
            </button>
          </Link>
          <Link to="/quiz">
            <button className="w-full bg-yellow-500 text-white py-3 px-6 rounded-lg shadow hover:bg-yellow-600 transition">
              Islamic Quiz
            </button>
          </Link>
        </div>
      </div>
    </div>
  );
};

export default Home;