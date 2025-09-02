import React, { useState, useEffect } from 'react';
import { Button } from '@/components/ui/button';
import { ArrowRight, Brain, Network, Shield, Zap, Eye, Cpu, Globe } from 'lucide-react';
import { motion, useScroll, useTransform } from 'framer-motion';
import heroBackground from '../assets/hero-background.png';
import neur1genesisLogo from '../assets/neur1genesis-logo.png';
import dashboardPreview from '../assets/dashboard-preview.png';
import echoNodeVisualization from '../assets/echo-node-visualization.png';

const LandingPage = ({ onEnterDashboard }) => {
  const [isVisible, setIsVisible] = useState({});
  const { scrollY } = useScroll();
  const y1 = useTransform(scrollY, [0, 300], [0, -50]);
  const y2 = useTransform(scrollY, [0, 300], [0, -100]);

  useEffect(() => {
    const observer = new IntersectionObserver(
      (entries) => {
        entries.forEach((entry) => {
          setIsVisible(prev => ({
            ...prev,
            [entry.target.id]: entry.isIntersecting
          }));
        });
      },
      { threshold: 0.1 }
    );

    document.querySelectorAll('[id]').forEach((el) => {
      observer.observe(el);
    });

    return () => observer.disconnect();
  }, []);

  const features = [
    {
      icon: Brain,
      title: "Autonomous EchoNodes",
      description: "Self-evolving AI agents with BDI-inspired contextual empathy and advanced reasoning capabilities."
    },
    {
      icon: Network,
      title: "Daedalus Coordinator",
      description: "Dynamic orchestration with natural language goal parsing and consensus-driven task allocation."
    },
    {
      icon: Shield,
      title: "Privacy-First PPSDS",
      description: "Privacy-Preserving Synthetic Data System ensuring ethical data handling and synthetic integrity."
    },
    {
      icon: Zap,
      title: "Neuro Adaptive Learning",
      description: "Advanced ANAL system with neuroplasticity simulation and catastrophic forgetting prevention."
    },
    {
      icon: Cpu,
      title: "InfiniGen Engine",
      description: "Self-evolving metaprogramming capabilities enabling true autonomous code evolution."
    },
    {
      icon: Globe,
      title: "Cross-Domain Intelligence",
      description: "Ethical inference, analogy-driven concept fusion, and intention cascading across contexts."
    }
  ];

  const capabilities = [
    "Real-time collaborative interfaces",
    "Voice, gesture, sketch & text input",
    "Transparent trust visualization",
    "Federated learning coordination",
    "Meta-reflection and self-awareness",
    "Ethical decision-making framework"
  ];

  return (
    <div className="min-h-screen bg-gradient-to-b from-slate-900 via-blue-900 to-slate-900 text-white overflow-hidden">
      {/* Hero Section */}
      <section className="relative min-h-screen flex items-center justify-center">
        <div 
          className="absolute inset-0 bg-cover bg-center bg-no-repeat opacity-30"
          style={{ backgroundImage: `url(${heroBackground})` }}
        />
        <div className="absolute inset-0 bg-gradient-to-b from-transparent via-slate-900/50 to-slate-900" />
        
        <motion.div 
          className="relative z-10 text-center px-4 max-w-6xl mx-auto"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 1 }}
        >
          <motion.img
            src={neur1genesisLogo}
            alt="Neur1Genesis Logo"
            className="w-32 h-32 mx-auto mb-8"
            style={{ y: y1 }}
            whileHover={{ scale: 1.05, rotate: 5 }}
            transition={{ type: "spring", stiffness: 300 }}
          />
          
          <motion.h1 
            className="text-6xl md:text-8xl font-bold mb-6 bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 bg-clip-text text-transparent"
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: 0.5, duration: 0.8 }}
          >
            Neur1Genesis
          </motion.h1>
          
          <motion.p 
            className="text-xl md:text-2xl mb-8 text-slate-300 max-w-4xl mx-auto leading-relaxed"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.8, duration: 0.8 }}
          >
            A futuristic Mixture of Autonomous Experts (MoAE) core intelligence engine composed of fully autonomous EchoNodes—empowered with contextual empathy, synthetic data integrity, and self-evolving metaprogramming capabilities.
          </motion.p>
          
          <motion.div
            className="flex flex-col sm:flex-row gap-4 justify-center items-center"
            initial={{ opacity: 0, y: 30 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: 1.2, duration: 0.8 }}
          >
            <Button
              onClick={onEnterDashboard}
              className="bg-gradient-to-r from-cyan-500 to-blue-600 hover:from-cyan-600 hover:to-blue-700 text-white px-8 py-4 text-lg font-semibold rounded-lg shadow-lg hover:shadow-cyan-500/25 transition-all duration-300 group"
            >
              Enter Dashboard
              <ArrowRight className="ml-2 h-5 w-5 group-hover:translate-x-1 transition-transform" />
            </Button>
            
            <Button
              variant="outline"
              className="border-cyan-400 text-cyan-400 hover:bg-cyan-400 hover:text-slate-900 px-8 py-4 text-lg font-semibold rounded-lg transition-all duration-300"
            >
              Learn More
            </Button>
          </motion.div>
        </motion.div>

        {/* Floating particles animation */}
        <div className="absolute inset-0 pointer-events-none">
          {[...Array(20)].map((_, i) => (
            <motion.div
              key={i}
              className="absolute w-1 h-1 bg-cyan-400 rounded-full"
              style={{
                left: `${Math.random() * 100}%`,
                top: `${Math.random() * 100}%`,
              }}
              animate={{
                y: [-20, -100, -20],
                opacity: [0, 1, 0],
              }}
              transition={{
                duration: 3 + Math.random() * 2,
                repeat: Infinity,
                delay: Math.random() * 2,
              }}
            />
          ))}
        </div>
      </section>

      {/* Features Section */}
      <section id="features" className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <motion.div
            className="text-center mb-16"
            initial={{ opacity: 0, y: 50 }}
            animate={isVisible.features ? { opacity: 1, y: 0 } : {}}
            transition={{ duration: 0.8 }}
          >
            <h2 className="text-4xl md:text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
              Core Intelligence Components
            </h2>
            <p className="text-xl text-slate-400 max-w-3xl mx-auto">
              Discover the revolutionary architecture that powers autonomous cognitive evolution
            </p>
          </motion.div>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
            {features.map((feature, index) => (
              <motion.div
                key={index}
                className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-xl p-6 hover:border-cyan-500/50 transition-all duration-300 group"
                initial={{ opacity: 0, y: 50 }}
                animate={isVisible.features ? { opacity: 1, y: 0 } : {}}
                transition={{ delay: index * 0.1, duration: 0.6 }}
                whileHover={{ scale: 1.02, y: -5 }}
              >
                <div className="flex items-center mb-4">
                  <div className="p-3 bg-gradient-to-r from-cyan-500/20 to-blue-500/20 rounded-lg group-hover:from-cyan-500/30 group-hover:to-blue-500/30 transition-all duration-300">
                    <feature.icon className="h-6 w-6 text-cyan-400" />
                  </div>
                </div>
                <h3 className="text-xl font-semibold mb-3 text-white group-hover:text-cyan-400 transition-colors">
                  {feature.title}
                </h3>
                <p className="text-slate-400 leading-relaxed">
                  {feature.description}
                </p>
              </motion.div>
            ))}
          </div>
        </div>
      </section>

      {/* Dashboard Preview Section */}
      <section id="dashboard-preview" className="py-20 px-4 bg-slate-900/50">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <motion.div
              initial={{ opacity: 0, x: -50 }}
              animate={isVisible['dashboard-preview'] ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8 }}
            >
              <h2 className="text-4xl md:text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
                Interactive 3D Dashboard
              </h2>
              <p className="text-xl text-slate-400 mb-8 leading-relaxed">
                Experience real-time visualization of your autonomous intelligence network with holographic interfaces, 
                trust consensus displays, and collaborative multi-modal interactions.
              </p>
              
              <div className="space-y-4">
                {capabilities.map((capability, index) => (
                  <motion.div
                    key={index}
                    className="flex items-center space-x-3"
                    initial={{ opacity: 0, x: -20 }}
                    animate={isVisible['dashboard-preview'] ? { opacity: 1, x: 0 } : {}}
                    transition={{ delay: index * 0.1, duration: 0.5 }}
                  >
                    <div className="w-2 h-2 bg-cyan-400 rounded-full" />
                    <span className="text-slate-300">{capability}</span>
                  </motion.div>
                ))}
              </div>
            </motion.div>

            <motion.div
              className="relative"
              initial={{ opacity: 0, x: 50 }}
              animate={isVisible['dashboard-preview'] ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8 }}
              style={{ y: y2 }}
            >
              <div className="relative rounded-xl overflow-hidden shadow-2xl">
                <img
                  src={dashboardPreview}
                  alt="Dashboard Preview"
                  className="w-full h-auto"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-900/50 to-transparent" />
              </div>
              
              {/* Floating UI elements */}
              <motion.div
                className="absolute -top-4 -right-4 w-16 h-16 bg-gradient-to-r from-cyan-500 to-blue-600 rounded-full flex items-center justify-center shadow-lg"
                animate={{ rotate: 360 }}
                transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
              >
                <Eye className="h-8 w-8 text-white" />
              </motion.div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* EchoNodes Network Section */}
      <section id="echonodes" className="py-20 px-4">
        <div className="max-w-7xl mx-auto">
          <div className="grid grid-cols-1 lg:grid-cols-2 gap-12 items-center">
            <motion.div
              className="relative order-2 lg:order-1"
              initial={{ opacity: 0, x: -50 }}
              animate={isVisible.echonodes ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8 }}
            >
              <div className="relative rounded-xl overflow-hidden shadow-2xl">
                <img
                  src={echoNodeVisualization}
                  alt="EchoNodes Network"
                  className="w-full h-auto"
                />
                <div className="absolute inset-0 bg-gradient-to-t from-slate-900/30 to-transparent" />
              </div>
            </motion.div>

            <motion.div
              className="order-1 lg:order-2"
              initial={{ opacity: 0, x: 50 }}
              animate={isVisible.echonodes ? { opacity: 1, x: 0 } : {}}
              transition={{ duration: 0.8 }}
            >
              <h2 className="text-4xl md:text-5xl font-bold mb-6 bg-gradient-to-r from-purple-400 to-cyan-400 bg-clip-text text-transparent">
                Autonomous EchoNodes Network
              </h2>
              <p className="text-xl text-slate-400 mb-8 leading-relaxed">
                Watch as intelligent agents collaborate, learn, and evolve in real-time. Each EchoNode operates with 
                contextual empathy, ethical reasoning, and self-improving capabilities through our advanced ANAL system.
              </p>
              
              <div className="grid grid-cols-2 gap-6">
                <div className="text-center">
                  <div className="text-3xl font-bold text-cyan-400 mb-2">∞</div>
                  <div className="text-sm text-slate-400">Scalable Nodes</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold text-blue-400 mb-2">24/7</div>
                  <div className="text-sm text-slate-400">Autonomous Operation</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold text-purple-400 mb-2">100%</div>
                  <div className="text-sm text-slate-400">Privacy Preserved</div>
                </div>
                <div className="text-center">
                  <div className="text-3xl font-bold text-green-400 mb-2">AI+</div>
                  <div className="text-sm text-slate-400">Self-Evolving</div>
                </div>
              </div>
            </motion.div>
          </div>
        </div>
      </section>

      {/* CTA Section */}
      <section className="py-20 px-4 bg-gradient-to-r from-slate-900 via-blue-900 to-slate-900">
        <motion.div
          className="max-w-4xl mx-auto text-center"
          initial={{ opacity: 0, y: 50 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.8 }}
        >
          <h2 className="text-4xl md:text-5xl font-bold mb-6 bg-gradient-to-r from-cyan-400 via-blue-400 to-purple-400 bg-clip-text text-transparent">
            Ready to Experience the Future?
          </h2>
          <p className="text-xl text-slate-300 mb-8 leading-relaxed">
            Step into the next generation of artificial intelligence with Neur1Genesis. 
            Witness autonomous cognition, ethical decision-making, and self-evolving intelligence.
          </p>
          
          <motion.div
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
          >
            <Button
              onClick={onEnterDashboard}
              className="bg-gradient-to-r from-cyan-500 via-blue-600 to-purple-600 hover:from-cyan-600 hover:via-blue-700 hover:to-purple-700 text-white px-12 py-6 text-xl font-bold rounded-xl shadow-2xl hover:shadow-cyan-500/25 transition-all duration-300 group"
            >
              Launch Dashboard
              <ArrowRight className="ml-3 h-6 w-6 group-hover:translate-x-2 transition-transform" />
            </Button>
          </motion.div>
        </motion.div>
      </section>

      {/* Footer */}
      <footer className="py-12 px-4 bg-slate-900 border-t border-slate-800">
        <div className="max-w-7xl mx-auto text-center">
          <img
            src={neur1genesisLogo}
            alt="Neur1Genesis"
            className="w-12 h-12 mx-auto mb-4 opacity-80"
          />
          <p className="text-slate-400 mb-4">
            Neur1Genesis - Pioneering Autonomous Intelligence Architecture
          </p>
          <p className="text-sm text-slate-500">
            Built with advanced AI, ethical frameworks, and self-evolving capabilities
          </p>
        </div>
      </footer>
    </div>
  );
};

export default LandingPage;

