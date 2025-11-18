import React, { useEffect, useState } from "react";
import { Link } from "react-router-dom";

const Hadith = () => {
  const [hadith, setHadith] = useState("");
  const [reference, setReference] = useState("");
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState("");

  const fetchHadith = async () => {
    try {
      setLoading(true);
      setError("");
      const res = await fetch("/api/hadith/random");
      const data = await res.json();
      if (res.ok) {
        setHadith(data.hadith);
        setReference(data.reference || "");
      } else {
        setError(data.error || "Could not fetch hadith");
      }
    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchHadith();
  }, []);

  return (
    <div
      className="min-h-screen relative bg-cover bg-center flex flex-col justify-center items-center p-6"
      style={{ backgroundImage: "url(/images/background3.jpg)" }}
    >
      {/* Top-left home button */}
      <div className="fixed top-4 left-4 z-50">
        <Link to="/">
          <button className="bg-yellow-600 hover:bg-yellow-500 transition-colors px-4 py-2 rounded shadow-lg font-semibold">
            &larr; Home
          </button>
        </Link>
      </div>

      <div className="relative z-10 max-w-3xl bg-black/40 backdrop-blur-md rounded-xl p-8 shadow-xl text-white text-center flex flex-col gap-4">
        <h1 className="text-4xl font-bold mb-4">Random Hadith</h1>

        {loading ? (
          <p className="text-yellow-200">Loading...</p>
        ) : error ? (
          <p className="text-red-400">{error}</p>
        ) : (
          <>
            <p className="text-lg">{hadith}</p>
            {reference && <p className="text-sm text-yellow-200 mt-2">{reference}</p>}
          </>
        )}

        <button
          onClick={fetchHadith}
          className="mt-4 bg-yellow-500 hover:bg-yellow-400 transition-colors px-6 py-2 rounded shadow-lg font-semibold"
        >
          Fetch New Hadith
        </button>
      </div>
    </div>
  );
};

export default Hadith;