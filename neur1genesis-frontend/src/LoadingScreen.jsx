import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import loadingAnimation from '../assets/loading-animation.png';

const LoadingScreen = ({ onLoadingComplete }) => {
  const [progress, setProgress] = useState(0);
  const [currentPhase, setCurrentPhase] = useState(0);
  const [isComplete, setIsComplete] = useState(false);

  const loadingPhases = [
    "Initializing EchoNodes...",
    "Activating Daedalus Coordinator...",
    "Loading PPSDS Framework...",
    "Calibrating ANAL Systems...",
    "Booting InfiniGen Engine...",
    "Establishing Cross-Domain Intelligence...",
    "Synchronizing Network Topology...",
    "Finalizing Holographic Interface..."
  ];

  useEffect(() => {
    const interval = setInterval(() => {
      setProgress(prev => {
        const newProgress = prev + Math.random() * 15 + 5;
        
        // Update phase based on progress
        const phaseIndex = Math.floor((newProgress / 100) * loadingPhases.length);
        setCurrentPhase(Math.min(phaseIndex, loadingPhases.length - 1));
        
        if (newProgress >= 100) {
          setIsComplete(true);
          clearInterval(interval);
          setTimeout(() => {
            onLoadingComplete();
          }, 1500);
          return 100;
        }
        
        return newProgress;
      });
    }, 200 + Math.random() * 300);

    return () => clearInterval(interval);
  }, [onLoadingComplete]);

  return (
    <AnimatePresence>
      <motion.div
        className="fixed inset-0 bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 flex items-center justify-center z-50"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        exit={{ opacity: 0 }}
        transition={{ duration: 0.5 }}
      >
        {/* Background particles */}
        <div className="absolute inset-0 overflow-hidden">
          {[...Array(50)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-cyan-400 rounded-full"
              style={{
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
              }}
              animate={{
                opacity: [0, 1, 0],
                scale: [0, 1, 0],
              }}
              transition={{
                duration: 2 + Math.random() * 3,
                repeat: Infinity,
                delay: Math.random() * 2,
              }}
            />
          ))}
        </div>

        <div className="relative z-10 text-center max-w-2xl mx-auto px-4">
          {/* Central Loading Animation */}
          <motion.div
            className="relative mb-12"
            initial={{ scale: 0, rotate: 0 }}
            animate={{ 
              scale: 1, 
              rotate: isComplete ? 360 : 0 
            }}
            transition={{ 
              scale: { duration: 1, ease: "easeOut" },
              rotate: { duration: 2, ease: "easeInOut" }
            }}
          >
            <div className="relative w-48 h-48 mx-auto">
              <img
                src={loadingAnimation}
                alt="Loading"
                className="w-full h-full object-contain"
              />
              
              {/* Rotating outer ring */}
              <motion.div
                className="absolute inset-0 border-2 border-transparent border-t-cyan-400 border-r-cyan-400 rounded-full"
                animate={{ rotate: 360 }}
                transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
              />
              
              {/* Pulsing inner ring */}
              <motion.div
                className="absolute inset-4 border border-blue-400 rounded-full"
                animate={{ 
                  scale: [1, 1.1, 1],
                  opacity: [0.5, 1, 0.5]
                }}
                transition={{ duration: 2, repeat: Infinity }}
              />
              
              {/* Center pulse */}
              <motion.div
                className="absolute inset-1/2 w-4 h-4 -ml-2 -mt-2 bg-cyan-400 rounded-full"
                animate={{ 
                  scale: [1, 1.5, 1],
                  opacity: [1, 0.3, 1]
                }}
                transition={{ duration: 1.5, repeat: Infinity }}
              />
            </div>
          </motion.div>

          {/* Progress Bar */}
          <div className="mb-8">
            <div className="w-full bg-slate-800 rounded-full h-2 mb-4">
              <motion.div
                className="bg-gradient-to-r from-cyan-400 to-blue-500 h-2 rounded-full relative overflow-hidden"
                initial={{ width: 0 }}
                animate={{ width: `${progress}%` }}
                transition={{ duration: 0.3 }}
              >
                {/* Progress bar glow effect */}
                <motion.div
                  className="absolute inset-0 bg-gradient-to-r from-transparent via-white to-transparent opacity-30"
                  animate={{ x: [-100, 300] }}
                  transition={{ duration: 1.5, repeat: Infinity }}
                />
              </motion.div>
            </div>
            
            <div className="flex justify-between text-sm text-slate-400">
              <span>Initializing</span>
              <span>{Math.round(progress)}%</span>
            </div>
          </div>

          {/* Loading Phase Text */}
          <motion.div
            className="mb-8"
            key={currentPhase}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.5 }}
          >
            <h2 className="text-2xl font-bold text-white mb-2">
              {loadingPhases[currentPhase]}
            </h2>
            <div className="flex justify-center space-x-1">
              {[...Array(3)].map((_, i) => (
                <motion.div
                  key={i}
                  className="w-2 h-2 bg-cyan-400 rounded-full"
                  animate={{ opacity: [0.3, 1, 0.3] }}
                  transition={{
                    duration: 1,
                    repeat: Infinity,
                    delay: i * 0.2
                  }}
                />
              ))}
            </div>
          </motion.div>

          {/* System Status Indicators */}
          <div className="grid grid-cols-2 md:grid-cols-4 gap-4 text-xs">
            {[
              { label: "EchoNodes", status: progress > 12 },
              { label: "Daedalus", status: progress > 25 },
              { label: "PPSDS", status: progress > 37 },
              { label: "ANAL", status: progress > 50 },
              { label: "InfiniGen", status: progress > 62 },
              { label: "Cross-Domain", status: progress > 75 },
              { label: "Network", status: progress > 87 },
              { label: "Interface", status: progress > 95 }
            ].map((system, index) => (
              <motion.div
                key={system.label}
                className={`p-2 rounded border ${
                  system.status 
                    ? 'border-green-400 bg-green-400/10 text-green-400' 
                    : 'border-slate-600 bg-slate-800/50 text-slate-400'
                }`}
                initial={{ opacity: 0, scale: 0.8 }}
                animate={{ opacity: 1, scale: 1 }}
                transition={{ delay: index * 0.1 }}
              >
                <div className="flex items-center justify-center space-x-1">
                  <div className={`w-2 h-2 rounded-full ${
                    system.status ? 'bg-green-400' : 'bg-slate-600'
                  }`} />
                  <span>{system.label}</span>
                </div>
              </motion.div>
            ))}
          </div>

          {/* Completion Message */}
          <AnimatePresence>
            {isComplete && (
              <motion.div
                className="absolute inset-0 flex items-center justify-center bg-slate-900/90"
                initial={{ opacity: 0 }}
                animate={{ opacity: 1 }}
                exit={{ opacity: 0 }}
              >
                <motion.div
                  className="text-center"
                  initial={{ scale: 0.8, opacity: 0 }}
                  animate={{ scale: 1, opacity: 1 }}
                  transition={{ duration: 0.5 }}
                >
                  <motion.div
                    className="w-16 h-16 mx-auto mb-4 border-2 border-green-400 rounded-full flex items-center justify-center"
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ delay: 0.2, type: "spring", stiffness: 200 }}
                  >
                    <motion.svg
                      className="w-8 h-8 text-green-400"
                      fill="none"
                      stroke="currentColor"
                      viewBox="0 0 24 24"
                      initial={{ pathLength: 0 }}
                      animate={{ pathLength: 1 }}
                      transition={{ delay: 0.5, duration: 0.5 }}
                    >
                      <motion.path
                        strokeLinecap="round"
                        strokeLinejoin="round"
                        strokeWidth={2}
                        d="M5 13l4 4L19 7"
                      />
                    </motion.svg>
                  </motion.div>
                  
                  <h3 className="text-2xl font-bold text-green-400 mb-2">
                    System Ready
                  </h3>
                  <p className="text-slate-300">
                    Entering Neur1Genesis Dashboard...
                  </p>
                </motion.div>
              </motion.div>
            )}
          </AnimatePresence>
        </div>

        {/* Corner decorations */}
        <div className="absolute top-4 left-4">
          <motion.div
            className="w-16 h-16 border-l-2 border-t-2 border-cyan-400"
            initial={{ opacity: 0, scale: 0 }}
            animate={{ opacity: 0.5, scale: 1 }}
            transition={{ delay: 0.5, duration: 1 }}
          />
        </div>
        
        <div className="absolute top-4 right-4">
          <motion.div
            className="w-16 h-16 border-r-2 border-t-2 border-cyan-400"
            initial={{ opacity: 0, scale: 0 }}
            animate={{ opacity: 0.5, scale: 1 }}
            transition={{ delay: 0.7, duration: 1 }}
          />
        </div>
        
        <div className="absolute bottom-4 left-4">
          <motion.div
            className="w-16 h-16 border-l-2 border-b-2 border-cyan-400"
            initial={{ opacity: 0, scale: 0 }}
            animate={{ opacity: 0.5, scale: 1 }}
            transition={{ delay: 0.9, duration: 1 }}
          />
        </div>
        
        <div className="absolute bottom-4 right-4">
          <motion.div
            className="w-16 h-16 border-r-2 border-b-2 border-cyan-400"
            initial={{ opacity: 0, scale: 0 }}
            animate={{ opacity: 0.5, scale: 1 }}
            transition={{ delay: 1.1, duration: 1 }}
          />
        </div>
      </motion.div>
    </AnimatePresence>
  );
};

export default LoadingScreen;

