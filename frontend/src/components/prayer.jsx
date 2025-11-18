import React, { useState } from "react";
import { Link } from "react-router-dom";

const Prayer = () => {
  const [city, setCity] = useState("");
  const [country, setCountry] = useState("");
  const [prayerTimes, setPrayerTimes] = useState(null);
  const [errorMessage, setErrorMessage] = useState("");
  const [methodName, setMethodName] = useState("ISNA");

  const methods = [
    "Muslim World League",
    "ISNA",
    "Egyptian",
    "Makkah",
    "Karachi",
    "Tehran"
  ];

  const handleSubmit = (e) => {
    e.preventDefault();
    // Fetch prayer times logic
  };

  const resetForm = () => {
    setCity("");
    setCountry("");
    setMethodName("ISNA");
    setPrayerTimes(null);
    setErrorMessage("");
  };

  return (
    <div
      className="relative min-h-screen bg-cover bg-center flex justify-center items-start p-6"
      style={{ backgroundImage: "url(/images/background2.jpg)" }}
    >
      {/* Overlay */}
      <div className="absolute inset-0 bg-gradient-to-b from-black/60 via-black/50 to-yellow-900/30"></div>

      {/* Main content */}
      <div className="relative z-10 w-full max-w-3xl text-white flex flex-col items-center">
        {/* Top-left home button */}
        <div className="fixed top-4 left-4 z-50">
          <Link to="/">
            <button className="bg-yellow-600 hover:bg-yellow-500 transition-colors px-4 py-2 rounded shadow-lg font-semibold">
              &larr; Home
            </button>
          </Link>
        </div>

        {/* Header */}
        <header className="text-center mt-12 mb-8">
          <h1 className="text-5xl md:text-6xl font-bold drop-shadow-lg">
            Prayer Times
          </h1>
          <p className="text-lg md:text-xl mt-2 text-yellow-200 drop-shadow">
            Enter your city and country to fetch today’s times
          </p>
        </header>

        {/* Form */}
        <section className="bg-black/30 backdrop-blur-md rounded-xl p-6 shadow-xl flex flex-col gap-6 w-full">
          {errorMessage && (
            <div className="text-red-400 font-semibold">{errorMessage}</div>
          )}

          <form onSubmit={handleSubmit} className="flex flex-col gap-4">
            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              <div className="flex flex-col">
                <label htmlFor="city" className="mb-1 font-medium">
                  City
                </label>
                <input
                  id="city"
                  type="text"
                  placeholder="e.g. London"
                  required
                  value={city}
                  onChange={(e) => setCity(e.target.value)}
                  className="px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400 text-black"
                />
              </div>

              <div className="flex flex-col">
                <label htmlFor="country" className="mb-1 font-medium">
                  Country
                </label>
                <input
                  id="country"
                  type="text"
                  placeholder="e.g. United Kingdom"
                  required
                  value={country}
                  onChange={(e) => setCountry(e.target.value)}
                  className="px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400 text-black"
                />
              </div>
            </div>

            <div className="flex flex-col md:flex-row md:items-center gap-4">
              <label htmlFor="method" className="font-medium">
                Calculation Method
              </label>
              <select
                name="method"
                id="method"
                value={methodName}
                onChange={(e) => setMethodName(e.target.value)}
                className="px-3 py-2 rounded-md focus:outline-none focus:ring-2 focus:ring-yellow-400 text-black"
              >
                {methods.map((method) => (
                  <option key={method} value={method}>
                    {method}
                  </option>
                ))}
              </select>
            </div>

            <div className="flex flex-col md:flex-row gap-4 mt-4">
              <button
                type="submit"
                className="bg-yellow-500 hover:bg-yellow-400 transition-colors px-6 py-2 rounded shadow-lg font-semibold"
              >
                Get Prayer Times
              </button>
              <button
                type="button"
                onClick={resetForm}
                className="bg-gray-700 hover:bg-gray-600 transition-colors px-6 py-2 rounded shadow-lg font-semibold"
              >
                Reset
              </button>
            </div>
          </form>

          {prayerTimes && (
            <div className="mt-6">
              <h2 className="text-2xl font-semibold">
                Prayer Times for {city}, {country}
              </h2>
              {/* Table of prayer times */}
            </div>
          )}
        </section>
      </div>
    </div>
  );
};

export default Prayer;