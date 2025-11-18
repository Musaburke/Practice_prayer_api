import React, { useState } from "react";
import { Link } from "react-router-dom";

const Tasbeeh = () => {
  const [subhanCount, setSubhanCount] = useState(0);
  const [alhamdCount, setAlhamdCount] = useState(0);
  const [akbarCount, setAkbarCount] = useState(0);

  const resetAll = () => {
    setSubhanCount(0);
    setAlhamdCount(0);
    setAkbarCount(0);
  };

  const incrementAll = () => {
    setSubhanCount(subhanCount + 1);
    setAlhamdCount(alhamdCount + 1);
    setAkbarCount(akbarCount + 1);
  };

  return (
    <div
      className="min-h-screen relative flex flex-col items-center justify-start p-6"
      style={{
        backgroundImage: "url(/images/background4.png)",
        backgroundSize: "cover",
        backgroundPosition: "center",
      }}
    >
      {/* Overlay for contrast */}
      <div className="absolute inset-0 bg-black/40"></div>

      {/* Top-left home button */}
      <div className="absolute top-4 left-4 z-20">
        <Link to="/">
          <button className="bg-yellow-600 hover:bg-yellow-500 transition-colors px-4 py-2 rounded shadow-lg font-semibold">
            &larr; Home
          </button>
        </Link>
      </div>

      <div className="relative z-10 w-full max-w-md text-center text-white flex flex-col items-center gap-6 mt-16">
        <h1 className="text-4xl md:text-5xl font-bold drop-shadow-lg">🌙 Tasbeeh Counter</h1>

        <div className="flex flex-col gap-4 w-full">
          <div className="flex justify-between items-center bg-black/30 p-4 rounded shadow-md">
            <button
              className="bg-yellow-500 hover:bg-yellow-400 transition-colors px-6 py-2 rounded font-semibold"
              onClick={() => setSubhanCount(subhanCount + 1)}
            >
              SubhanAllah
            </button>
            <div className="text-2xl font-bold">{subhanCount}</div>
          </div>

          <div className="flex justify-between items-center bg-black/30 p-4 rounded shadow-md">
            <button
              className="bg-yellow-500 hover:bg-yellow-400 transition-colors px-6 py-2 rounded font-semibold"
              onClick={() => setAlhamdCount(alhamdCount + 1)}
            >
              Alhamdulillah
            </button>
            <div className="text-2xl font-bold">{alhamdCount}</div>
          </div>

          <div className="flex justify-between items-center bg-black/30 p-4 rounded shadow-md">
            <button
              className="bg-yellow-500 hover:bg-yellow-400 transition-colors px-6 py-2 rounded font-semibold"
              onClick={() => setAkbarCount(akbarCount + 1)}
            >
              Allahu Akbar
            </button>
            <div className="text-2xl font-bold">{akbarCount}</div>
          </div>
        </div>

        {/* Increment all counters button */}
        <button
          className="bg-orange-400 hover:bg-orange-300 transition-colors px-6 py-2 rounded shadow-lg font-semibold mt-2"
          onClick={incrementAll}
        >
          Add 1 to All
        </button>

        <button
          className="bg-gray-700 hover:bg-gray-600 transition-colors px-6 py-2 rounded shadow-lg font-semibold mt-2"
          onClick={resetAll}
        >
          Reset All
        </button>
      </div>
    </div>
  );
};

export default Tasbeeh;