import React, { useState } from 'react';
import { AnimatePresence } from 'framer-motion';
import LandingPage from './components/LandingPage';
import LoadingScreen from './components/LoadingScreen';
import Dashboard from './components/Dashboard';
import './App.css';

function App() {
  const [currentView, setCurrentView] = useState('landing'); // 'landing', 'loading', 'dashboard'

  const handleEnterDashboard = () => {
    setCurrentView('loading');
  };

  const handleLoadingComplete = () => {
    setCurrentView('dashboard');
  };

  const handleBackToLanding = () => {
    setCurrentView('landing');
  };

  return (
    <div className="App">
      <AnimatePresence mode="wait">
        {currentView === 'landing' && (
          <LandingPage 
            key="landing"
            onEnterDashboard={handleEnterDashboard}
          />
        )}
        
        {currentView === 'loading' && (
          <LoadingScreen 
            key="loading"
            onLoadingComplete={handleLoadingComplete}
          />
        )}
        
        {currentView === 'dashboard' && (
          <Dashboard 
            key="dashboard"
            onBackToLanding={handleBackToLanding}
          />
        )}
      </AnimatePresence>
    </div>
  );
}

export default App;
