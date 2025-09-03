import React, { useState, useEffect, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { 
  Brain, Network, Shield, Zap, Cpu, Globe, 
  Activity, Users, Settings, Menu, X, 
  Eye, Mic, PenTool, MessageSquare,
  TrendingUp, AlertTriangle, CheckCircle,
  BarChart3, PieChart, LineChart
} from 'lucide-react';
import { Button } from '@/components/ui/button';

const Dashboard = ({ onBackToLanding }) => {
  const [activePanel, setActivePanel] = useState('overview');
  const [sidebarOpen, setSidebarOpen] = useState(false);
  const [echoNodes, setEchoNodes] = useState([]);
  const [systemMetrics, setSystemMetrics] = useState({
    activeNodes: 0,
    totalTasks: 0,
    successRate: 0,
    networkHealth: 0
  });
  const [realTimeData, setRealTimeData] = useState([]);
  const canvasRef = useRef(null);

  // Simulate real-time data updates
  useEffect(() => {
    const interval = setInterval(() => {
      setSystemMetrics(prev => ({
        activeNodes: Math.floor(Math.random() * 20) + 5,
        totalTasks: Math.floor(Math.random() * 1000) + 500,
        successRate: Math.random() * 20 + 80,
        networkHealth: Math.random() * 30 + 70
      }));

      setRealTimeData(prev => {
        const newData = [...prev.slice(-19), {
          timestamp: Date.now(),
          value: Math.random() * 100,
          nodes: Math.floor(Math.random() * 10) + 5
        }];
        return newData;
      });
    }, 2000);

    return () => clearInterval(interval);
  }, []);

  // Initialize EchoNodes
  useEffect(() => {
    const nodes = Array.from({ length: 8 }, (_, i) => ({
      id: `node-${i}`,
      name: `EchoNode-${i + 1}`,
      status: Math.random() > 0.2 ? 'active' : 'idle',
      load: Math.random() * 100,
      connections: Math.floor(Math.random() * 15) + 3,
      x: Math.random() * 400 + 100,
      y: Math.random() * 300 + 100
    }));
    setEchoNodes(nodes);
  }, []);

  // Canvas animation for network visualization
  useEffect(() => {
    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    const resizeCanvas = () => {
      canvas.width = canvas.offsetWidth;
      canvas.height = canvas.offsetHeight;
    };
    
    resizeCanvas();
    window.addEventListener('resize', resizeCanvas);

    let animationId;
    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      // Draw connections between nodes
      echoNodes.forEach((node, i) => {
        echoNodes.slice(i + 1).forEach(otherNode => {
          if (Math.random() > 0.7) {
            const gradient = ctx.createLinearGradient(node.x, node.y, otherNode.x, otherNode.y);
            gradient.addColorStop(0, 'rgba(34, 211, 238, 0.3)');
            gradient.addColorStop(1, 'rgba(59, 130, 246, 0.1)');
            
            ctx.strokeStyle = gradient;
            ctx.lineWidth = 1;
            ctx.beginPath();
            ctx.moveTo(node.x, node.y);
            ctx.lineTo(otherNode.x, otherNode.y);
            ctx.stroke();
          }
        });
      });

      // Draw nodes
      echoNodes.forEach(node => {
        const radius = node.status === 'active' ? 8 : 5;
        const color = node.status === 'active' ? '#22d3ee' : '#64748b';
        
        ctx.beginPath();
        ctx.arc(node.x, node.y, radius, 0, Math.PI * 2);
        ctx.fillStyle = color;
        ctx.fill();
        
        // Pulsing effect for active nodes
        if (node.status === 'active') {
          ctx.beginPath();
          ctx.arc(node.x, node.y, radius + Math.sin(Date.now() / 1000) * 3, 0, Math.PI * 2);
          ctx.strokeStyle = 'rgba(34, 211, 238, 0.3)';
          ctx.lineWidth = 2;
          ctx.stroke();
        }
      });

      animationId = requestAnimationFrame(animate);
    };

    animate();

    return () => {
      window.removeEventListener('resize', resizeCanvas);
      cancelAnimationFrame(animationId);
    };
  }, [echoNodes]);

  const menuItems = [
    { id: 'overview', label: 'System Overview', icon: Activity },
    { id: 'echonodes', label: 'EchoNodes', icon: Brain },
    { id: 'network', label: 'Network Topology', icon: Network },
    { id: 'analytics', label: 'Analytics', icon: BarChart3 },
    { id: 'security', label: 'Security & Privacy', icon: Shield },
    { id: 'learning', label: 'ANAL Systems', icon: Zap },
    { id: 'evolution', label: 'InfiniGen Engine', icon: Cpu },
    { id: 'ethics', label: 'Cross-Domain AI', icon: Globe },
    { id: 'settings', label: 'Settings', icon: Settings }
  ];

  const collaborativeInterfaces = [
    { icon: MessageSquare, label: 'Text Input', active: true },
    { icon: Mic, label: 'Voice Control', active: false },
    { icon: Eye, label: 'Gesture Recognition', active: false },
    { icon: PenTool, label: 'Sketch Interface', active: false }
  ];

  const renderOverview = () => (
    <div className="space-y-6">
      {/* System Status Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {[
          { 
            title: 'Active EchoNodes', 
            value: systemMetrics.activeNodes, 
            icon: Brain, 
            color: 'text-cyan-400',
            bgColor: 'bg-cyan-400/10'
          },
          { 
            title: 'Total Tasks', 
            value: systemMetrics.totalTasks, 
            icon: Activity, 
            color: 'text-blue-400',
            bgColor: 'bg-blue-400/10'
          },
          { 
            title: 'Success Rate', 
            value: `${systemMetrics.successRate.toFixed(1)}%`, 
            icon: CheckCircle, 
            color: 'text-green-400',
            bgColor: 'bg-green-400/10'
          },
          { 
            title: 'Network Health', 
            value: `${systemMetrics.networkHealth.toFixed(1)}%`, 
            icon: TrendingUp, 
            color: 'text-purple-400',
            bgColor: 'bg-purple-400/10'
          }
        ].map((metric, index) => (
          <motion.div
            key={metric.title}
            className={`${metric.bgColor} backdrop-blur-sm border border-slate-700 rounded-xl p-6 hover:border-cyan-500/50 transition-all duration-300`}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02, y: -2 }}
          >
            <div className="flex items-center justify-between mb-4">
              <metric.icon className={`h-8 w-8 ${metric.color}`} />
              <div className={`text-2xl font-bold ${metric.color}`}>
                {metric.value}
              </div>
            </div>
            <h3 className="text-sm font-medium text-slate-300">{metric.title}</h3>
          </motion.div>
        ))}
      </div>

      {/* Network Visualization */}
      <motion.div
        className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-xl p-6"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.4 }}
      >
        <h3 className="text-xl font-semibold text-white mb-4 flex items-center">
          <Network className="h-6 w-6 text-cyan-400 mr-2" />
          Real-time Network Topology
        </h3>
        <div className="relative h-96 bg-slate-900/50 rounded-lg overflow-hidden">
          <canvas
            ref={canvasRef}
            className="absolute inset-0 w-full h-full"
            style={{ background: 'transparent' }}
          />
          
          {/* Network Stats Overlay */}
          <div className="absolute top-4 right-4 bg-slate-800/80 backdrop-blur-sm rounded-lg p-3">
            <div className="text-sm space-y-1">
              <div className="flex items-center justify-between">
                <span className="text-slate-400">Active Connections:</span>
                <span className="text-cyan-400 font-semibold">
                  {echoNodes.reduce((sum, node) => sum + node.connections, 0)}
                </span>
              </div>
              <div className="flex items-center justify-between">
                <span className="text-slate-400">Network Load:</span>
                <span className="text-blue-400 font-semibold">
                  {Math.round(echoNodes.reduce((sum, node) => sum + node.load, 0) / echoNodes.length)}%
                </span>
              </div>
            </div>
          </div>
        </div>
      </motion.div>

      {/* Collaborative Interfaces */}
      <motion.div
        className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-xl p-6"
        initial={{ opacity: 0, y: 20 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ delay: 0.6 }}
      >
        <h3 className="text-xl font-semibold text-white mb-4">
          Collaborative Interfaces
        </h3>
        <div className="grid grid-cols-2 md:grid-cols-4 gap-4">
          {collaborativeInterfaces.map((interfaceItem, index) => (
            <motion.div
              key={interfaceItem.label}
              className={`p-4 rounded-lg border transition-all duration-300 cursor-pointer ${
                interfaceItem.active 
                  ? 'border-cyan-500 bg-cyan-500/10 text-cyan-400' 
                  : 'border-slate-600 bg-slate-800/50 text-slate-400 hover:border-slate-500'
              }`}
              whileHover={{ scale: 1.02 }}
              whileTap={{ scale: 0.98 }}
            >
              <interfaceItem.icon className="h-8 w-8 mx-auto mb-2" />
              <div className="text-center text-sm font-medium">
                {interfaceItem.label}
              </div>
              {interfaceItem.active && (
                <motion.div
                  className="w-2 h-2 bg-green-400 rounded-full mx-auto mt-2"
                  animate={{ scale: [1, 1.2, 1] }}
                  transition={{ duration: 2, repeat: Infinity }}
                />
              )}
            </motion.div>
          ))}
        </div>
      </motion.div>
    </div>
  );

  const renderEchoNodes = () => (
    <div className="space-y-6">
      <div className="flex items-center justify-between">
        <h2 className="text-2xl font-bold text-white">EchoNodes Management</h2>
        <Button className="bg-cyan-500 hover:bg-cyan-600">
          Deploy New Node
        </Button>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        {echoNodes.map((node, index) => (
          <motion.div
            key={node.id}
            className="bg-slate-800/50 backdrop-blur-sm border border-slate-700 rounded-xl p-6 hover:border-cyan-500/50 transition-all duration-300"
            initial={{ opacity: 0, scale: 0.9 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay: index * 0.1 }}
            whileHover={{ scale: 1.02, y: -2 }}
          >
            <div className="flex items-center justify-between mb-4">
              <h3 className="text-lg font-semibold text-white">{node.name}</h3>
              <div className={`w-3 h-3 rounded-full ${
                node.status === 'active' ? 'bg-green-400' : 'bg-slate-500'
              }`} />
            </div>
            
            <div className="space-y-3">
              <div className="flex justify-between text-sm">
                <span className="text-slate-400">Status:</span>
                <span className={node.status === 'active' ? 'text-green-400' : 'text-slate-400'}>
                  {node.status.charAt(0).toUpperCase() + node.status.slice(1)}
                </span>
              </div>
              
              <div className="flex justify-between text-sm">
                <span className="text-slate-400">Load:</span>
                <span className="text-cyan-400">{Math.round(node.load)}%</span>
              </div>
              
              <div className="flex justify-between text-sm">
                <span className="text-slate-400">Connections:</span>
                <span className="text-blue-400">{node.connections}</span>
              </div>

              {/* Load bar */}
              <div className="w-full bg-slate-700 rounded-full h-2">
                <motion.div
                  className="bg-gradient-to-r from-cyan-400 to-blue-500 h-2 rounded-full"
                  initial={{ width: 0 }}
                  animate={{ width: `${node.load}%` }}
                  transition={{ duration: 1, delay: index * 0.1 }}
                />
              </div>
            </div>
          </motion.div>
        ))}
      </div>
    </div>
  );

  const renderContent = () => {
    switch (activePanel) {
      case 'overview':
        return renderOverview();
      case 'echonodes':
        return renderEchoNodes();
      case 'network':
        return (
          <div className="text-center py-20">
            <Network className="h-16 w-16 text-cyan-400 mx-auto mb-4" />
            <h2 className="text-2xl font-bold text-white mb-2">Network Topology</h2>
            <p className="text-slate-400">Advanced network visualization coming soon...</p>
          </div>
        );
      case 'analytics':
        return (
          <div className="text-center py-20">
            <BarChart3 className="h-16 w-16 text-blue-400 mx-auto mb-4" />
            <h2 className="text-2xl font-bold text-white mb-2">Analytics Dashboard</h2>
            <p className="text-slate-400">Comprehensive analytics and insights coming soon...</p>
          </div>
        );
      default:
        return (
          <div className="text-center py-20">
            <div className="h-16 w-16 bg-slate-700 rounded-lg mx-auto mb-4 flex items-center justify-center">
              <Settings className="h-8 w-8 text-slate-400" />
            </div>
            <h2 className="text-2xl font-bold text-white mb-2">
              {menuItems.find(item => item.id === activePanel)?.label}
            </h2>
            <p className="text-slate-400">This section is under development...</p>
          </div>
        );
    }
  };

  return (
    <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 text-white">
      {/* Header */}
      <header className="bg-slate-800/50 backdrop-blur-sm border-b border-slate-700 px-4 py-4">
        <div className="flex items-center justify-between">
          <div className="flex items-center space-x-4">
            <Button
              variant="ghost"
              size="sm"
              onClick={() => setSidebarOpen(!sidebarOpen)}
              className="lg:hidden text-white hover:bg-slate-700"
            >
              <Menu className="h-5 w-5" />
            </Button>
            
            <h1 className="text-2xl font-bold bg-gradient-to-r from-cyan-400 to-blue-400 bg-clip-text text-transparent">
              Neur1Genesis Dashboard
            </h1>
          </div>

          <div className="flex items-center space-x-4">
            <div className="hidden md:flex items-center space-x-2 text-sm">
              <div className="w-2 h-2 bg-green-400 rounded-full animate-pulse" />
              <span className="text-slate-300">System Online</span>
            </div>
            
            <Button
              variant="outline"
              size="sm"
              onClick={onBackToLanding}
              className="border-slate-600 text-slate-300 hover:bg-slate-700"
            >
              Exit Dashboard
            </Button>
          </div>
        </div>
      </header>

      <div className="flex">
        {/* Sidebar */}
        <AnimatePresence>
          {(sidebarOpen || window.innerWidth >= 1024) && (
            <motion.aside
              className="fixed lg:relative inset-y-0 left-0 z-50 w-64 bg-slate-800/50 backdrop-blur-sm border-r border-slate-700 lg:translate-x-0"
              initial={{ x: -256 }}
              animate={{ x: 0 }}
              exit={{ x: -256 }}
              transition={{ type: "spring", stiffness: 300, damping: 30 }}
            >
              <div className="p-4">
                <div className="flex items-center justify-between lg:hidden mb-4">
                  <span className="text-lg font-semibold">Menu</span>
                  <Button
                    variant="ghost"
                    size="sm"
                    onClick={() => setSidebarOpen(false)}
                    className="text-white hover:bg-slate-700"
                  >
                    <X className="h-5 w-5" />
                  </Button>
                </div>

                <nav className="space-y-2">
                  {menuItems.map((item) => (
                    <motion.button
                      key={item.id}
                      onClick={() => {
                        setActivePanel(item.id);
                        setSidebarOpen(false);
                      }}
                      className={`w-full flex items-center space-x-3 px-3 py-2 rounded-lg text-left transition-all duration-200 ${
                        activePanel === item.id
                          ? 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/30'
                          : 'text-slate-300 hover:bg-slate-700/50 hover:text-white'
                      }`}
                      whileHover={{ scale: 1.02 }}
                      whileTap={{ scale: 0.98 }}
                    >
                      <item.icon className="h-5 w-5" />
                      <span>{item.label}</span>
                    </motion.button>
                  ))}
                </nav>
              </div>
            </motion.aside>
          )}
        </AnimatePresence>

        {/* Main Content */}
        <main className="flex-1 p-6 lg:p-8">
          <motion.div
            key={activePanel}
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            transition={{ duration: 0.3 }}
          >
            {renderContent()}
          </motion.div>
        </main>
      </div>

      {/* Mobile sidebar overlay */}
      <AnimatePresence>
        {sidebarOpen && (
          <motion.div
            className="fixed inset-0 bg-black/50 z-40 lg:hidden"
            initial={{ opacity: 0 }}
            animate={{ opacity: 1 }}
            exit={{ opacity: 0 }}
            onClick={() => setSidebarOpen(false)}
          />
        )}
      </AnimatePresence>
    </div>
  );
};

export default Dashboard;

