import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Home from "./components/home";
import Prayer from "./components/prayer";
import Tasbeeh from "./components/tasbeeh";

const App = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/prayer" element={<Prayer />} />
        <Route path="/tasbeeh" element={<Tasbeeh />} />
      </Routes>
    </Router>
  );
};

export default App;