import json
import uuid
import logging
import numpy as np
from datetime import datetime
from typing import Dict, List, Any, Optional, Tuple, Callable
from dataclasses import dataclass, asdict
from enum import Enum
import copy

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class LearningMode(Enum):
    SUPERVISED = "supervised"
    UNSUPERVISED = "unsupervised"
    REINFORCEMENT = "reinforcement"
    CONTINUAL = "continual"
    FEDERATED = "federated"

class AdaptationStrategy(Enum):
    GRADIENT_BASED = "gradient_based"
    EVOLUTIONARY = "evolutionary"
    NEUROPLASTICITY = "neuroplasticity"
    META_LEARNING = "meta_learning"

@dataclass
class LearningExperience:
    """Represents a learning experience"""
    experience_id: str
    input_data: Dict[str, Any]
    expected_output: Optional[Dict[str, Any]]
    actual_output: Dict[str, Any]
    reward: Optional[float]
    context: Dict[str, Any]
    timestamp: datetime

@dataclass
class AdaptationResult:
    """Result of an adaptation process"""
    adaptation_id: str
    strategy_used: AdaptationStrategy
    parameters_updated: List[str]
    performance_improvement: float
    confidence: float
    metadata: Dict[str, Any]
    timestamp: datetime

@dataclass
class NeuralConnection:
    """Represents a neural connection for neuroplasticity simulation"""
    connection_id: str
    source_node: str
    target_node: str
    weight: float
    strength: float
    last_activation: datetime
    plasticity_factor: float

class NeuroAdaptiveLearning:
    """
    ANAL (Neuro Adaptive Learning) Module
    Implements continuous learning, adaptive model updates, neuroplasticity simulation,
    and prevents catastrophic forgetting through advanced learning techniques.
    """
    
    def __init__(self, node_id: str, learning_config: Dict[str, Any] = None):
        self.node_id = node_id
        self.learning_id = str(uuid.uuid4())
        
        # Learning configuration
        self.learning_config = learning_config or {
            "learning_rate": 0.01,
            "adaptation_threshold": 0.1,
            "memory_consolidation_rate": 0.05,
            "plasticity_decay": 0.99,
            "catastrophic_forgetting_prevention": True,
            "meta_learning_enabled": True,
            "neuroplasticity_enabled": True
        }
        
        # Learning state
        self.current_mode = LearningMode.CONTINUAL
        self.adaptation_strategy = AdaptationStrategy.NEUROPLASTICITY
        
        # Experience memory for continual learning
        self.experience_buffer: List[LearningExperience] = []
        self.max_experience_buffer_size = 1000
        
        # Model parameters and weights
        self.model_parameters: Dict[str, Any] = {
            "weights": {},
            "biases": {},
            "activation_functions": {},
            "layer_configurations": {}
        }
        
        # Neuroplasticity simulation
        self.neural_connections: Dict[str, NeuralConnection] = {}
        self.synaptic_plasticity_rules = {
            "hebbian": True,
            "spike_timing_dependent": True,
            "homeostatic": True
        }
        
        # Catastrophic forgetting prevention
        self.importance_weights: Dict[str, float] = {}
        self.previous_task_parameters: Dict[str, Dict[str, Any]] = {}
        
        # Meta-learning components
        self.meta_parameters: Dict[str, Any] = {
            "learning_rate_adaptation": 0.001,
            "task_similarity_threshold": 0.7,
            "adaptation_speed": 1.0
        }
        
        # Performance tracking
        self.performance_history: List[Dict[str, Any]] = []
        self.adaptation_history: List[AdaptationResult] = []
        
        # Federated learning state
        self.federated_updates: List[Dict[str, Any]] = []
        
        logger.info(f"ANAL module initialized for node {self.node_id}")
    
    def learn_from_experience(self, experience: LearningExperience) -> Dict[str, Any]:
        """
        Learn from a single experience using continual learning principles
        """
        # Add experience to buffer
        self.experience_buffer.append(experience)
        
        # Maintain buffer size
        if len(self.experience_buffer) > self.max_experience_buffer_size:
            self.experience_buffer.pop(0)  # Remove oldest experience
        
        # Determine learning approach based on experience type
        learning_result = {}
        
        if experience.expected_output is not None:
            # Supervised learning
            learning_result = self._supervised_learning_update(experience)
        elif experience.reward is not None:
            # Reinforcement learning
            learning_result = self._reinforcement_learning_update(experience)
        else:
            # Unsupervised learning
            learning_result = self._unsupervised_learning_update(experience)
        
        # Apply neuroplasticity updates
        if self.learning_config["neuroplasticity_enabled"]:
            plasticity_result = self._apply_neuroplasticity(experience)
            learning_result["neuroplasticity"] = plasticity_result
        
        # Prevent catastrophic forgetting
        if self.learning_config["catastrophic_forgetting_prevention"]:
            forgetting_prevention = self._prevent_catastrophic_forgetting(experience)
            learning_result["forgetting_prevention"] = forgetting_prevention
        
        # Update performance tracking
        self._update_performance_tracking(experience, learning_result)
        
        logger.info(f"ANAL learned from experience {experience.experience_id}")
        return learning_result
    
    def _supervised_learning_update(self, experience: LearningExperience) -> Dict[str, Any]:
        """Update model using supervised learning"""
        # Calculate error/loss
        error = self._calculate_prediction_error(
            experience.expected_output, 
            experience.actual_output
        )
        
        # Update model parameters using gradient-like approach
        parameter_updates = {}
        learning_rate = self.learning_config["learning_rate"]
        
        for param_name in self.model_parameters["weights"]:
            # Simulate gradient update
            gradient = error * 0.1 * np.random.normal(0, 0.1)  # Simplified gradient
            old_value = self.model_parameters["weights"].get(param_name, 0.0)
            new_value = old_value - learning_rate * gradient
            
            self.model_parameters["weights"][param_name] = new_value
            parameter_updates[param_name] = {
                "old_value": old_value,
                "new_value": new_value,
                "gradient": gradient
            }
        
        return {
            "learning_type": "supervised",
            "error": error,
            "parameter_updates": parameter_updates,
            "learning_rate_used": learning_rate
        }
    
    def _reinforcement_learning_update(self, experience: LearningExperience) -> Dict[str, Any]:
        """Update model using reinforcement learning"""
        reward = experience.reward
        
        # Update value function or policy based on reward
        value_update = {}
        policy_update = {}
        
        # Simulate Q-learning style update
        learning_rate = self.learning_config["learning_rate"]
        discount_factor = 0.95
        
        # Update action values
        for action_key in experience.actual_output:
            old_q_value = self.model_parameters["weights"].get(f"q_{action_key}", 0.0)
            
            # Simplified Q-learning update
            new_q_value = old_q_value + learning_rate * (reward - old_q_value)
            
            self.model_parameters["weights"][f"q_{action_key}"] = new_q_value
            value_update[action_key] = {
                "old_q_value": old_q_value,
                "new_q_value": new_q_value,
                "reward": reward
            }
        
        return {
            "learning_type": "reinforcement",
            "reward": reward,
            "value_updates": value_update,
            "policy_updates": policy_update
        }
    
    def _unsupervised_learning_update(self, experience: LearningExperience) -> Dict[str, Any]:
        """Update model using unsupervised learning"""
        # Extract patterns from input data
        patterns = self._extract_patterns(experience.input_data)
        
        # Update internal representations
        representation_updates = {}
        
        for pattern_name, pattern_value in patterns.items():
            # Update internal representation weights
            old_weight = self.model_parameters["weights"].get(f"repr_{pattern_name}", 0.0)
            adaptation_rate = self.learning_config["learning_rate"] * 0.5
            
            new_weight = old_weight + adaptation_rate * (pattern_value - old_weight)
            
            self.model_parameters["weights"][f"repr_{pattern_name}"] = new_weight
            representation_updates[pattern_name] = {
                "old_weight": old_weight,
                "new_weight": new_weight,
                "pattern_value": pattern_value
            }
        
        return {
            "learning_type": "unsupervised",
            "patterns_extracted": patterns,
            "representation_updates": representation_updates
        }
    
    def _calculate_prediction_error(self, expected: Dict[str, Any], 
                                  actual: Dict[str, Any]) -> float:
        """Calculate prediction error between expected and actual outputs"""
        total_error = 0.0
        num_comparisons = 0
        
        for key in expected:
            if key in actual:
                try:
                    expected_val = float(expected[key])
                    actual_val = float(actual[key])
                    error = abs(expected_val - actual_val)
                    total_error += error
                    num_comparisons += 1
                except (ValueError, TypeError):
                    # Handle non-numeric values
                    if expected[key] != actual[key]:
                        total_error += 1.0
                    num_comparisons += 1
        
        return total_error / max(num_comparisons, 1)
    
    def _extract_patterns(self, input_data: Dict[str, Any]) -> Dict[str, float]:
        """Extract patterns from input data for unsupervised learning"""
        patterns = {}
        
        # Simple pattern extraction
        for key, value in input_data.items():
            try:
                numeric_value = float(value)
                patterns[f"magnitude_{key}"] = abs(numeric_value)
                patterns[f"sign_{key}"] = 1.0 if numeric_value >= 0 else -1.0
            except (ValueError, TypeError):
                # Handle non-numeric values
                patterns[f"presence_{key}"] = 1.0 if value else 0.0
                patterns[f"length_{key}"] = float(len(str(value)))
        
        return patterns
    
    def _apply_neuroplasticity(self, experience: LearningExperience) -> Dict[str, Any]:
        """
        Apply neuroplasticity rules to simulate synaptic changes
        """
        plasticity_updates = {
            "connections_strengthened": [],
            "connections_weakened": [],
            "new_connections": [],
            "pruned_connections": []
        }
        
        # Simulate Hebbian learning: "neurons that fire together, wire together"
        if self.synaptic_plasticity_rules["hebbian"]:
            for connection_id, connection in self.neural_connections.items():
                # Simulate co-activation
                activation_correlation = np.random.random()  # Simplified
                
                if activation_correlation > 0.7:
                    # Strengthen connection
                    old_weight = connection.weight
                    connection.weight *= (1 + self.learning_config["learning_rate"])
                    connection.strength = min(connection.strength * 1.1, 1.0)
                    
                    plasticity_updates["connections_strengthened"].append({
                        "connection_id": connection_id,
                        "old_weight": old_weight,
                        "new_weight": connection.weight
                    })
                
                elif activation_correlation < 0.3:
                    # Weaken connection
                    old_weight = connection.weight
                    connection.weight *= (1 - self.learning_config["learning_rate"] * 0.5)
                    connection.strength = max(connection.strength * 0.95, 0.1)
                    
                    plasticity_updates["connections_weakened"].append({
                        "connection_id": connection_id,
                        "old_weight": old_weight,
                        "new_weight": connection.weight
                    })
        
        # Create new connections based on experience
        if len(self.neural_connections) < 100:  # Limit total connections
            new_connection = NeuralConnection(
                connection_id=str(uuid.uuid4()),
                source_node=f"input_{len(experience.input_data)}",
                target_node=f"output_{len(experience.actual_output)}",
                weight=np.random.normal(0, 0.1),
                strength=0.5,
                last_activation=datetime.utcnow(),
                plasticity_factor=1.0
            )
            
            self.neural_connections[new_connection.connection_id] = new_connection
            plasticity_updates["new_connections"].append(new_connection.connection_id)
        
        # Prune weak connections
        connections_to_prune = [
            conn_id for conn_id, conn in self.neural_connections.items()
            if conn.strength < 0.2
        ]
        
        for conn_id in connections_to_prune[:5]:  # Limit pruning per iteration
            del self.neural_connections[conn_id]
            plasticity_updates["pruned_connections"].append(conn_id)
        
        return plasticity_updates
    
    def _prevent_catastrophic_forgetting(self, experience: LearningExperience) -> Dict[str, Any]:
        """
        Implement Elastic Weight Consolidation (EWC) to prevent catastrophic forgetting
        """
        forgetting_prevention = {
            "importance_weights_updated": {},
            "parameter_constraints": {},
            "memory_consolidation": {}
        }
        
        # Update importance weights for parameters
        for param_name in self.model_parameters["weights"]:
            # Calculate importance based on parameter usage
            current_importance = self.importance_weights.get(param_name, 0.0)
            
            # Increase importance if parameter was significantly used
            param_value = abs(self.model_parameters["weights"][param_name])
            if param_value > 0.1:  # Threshold for significant usage
                new_importance = current_importance + self.learning_config["memory_consolidation_rate"]
                self.importance_weights[param_name] = min(new_importance, 1.0)
                
                forgetting_prevention["importance_weights_updated"][param_name] = {
                    "old_importance": current_importance,
                    "new_importance": self.importance_weights[param_name]
                }
        
        # Apply constraints to important parameters
        for param_name, importance in self.importance_weights.items():
            if importance > 0.5:  # High importance threshold
                # Constrain parameter changes
                if param_name in self.previous_task_parameters:
                    previous_value = self.previous_task_parameters[param_name]
                    current_value = self.model_parameters["weights"].get(param_name, 0.0)
                    
                    # Apply elastic constraint
                    max_change = (1.0 - importance) * 0.1
                    if abs(current_value - previous_value) > max_change:
                        # Constrain the change
                        direction = 1 if current_value > previous_value else -1
                        constrained_value = previous_value + direction * max_change
                        
                        self.model_parameters["weights"][param_name] = constrained_value
                        
                        forgetting_prevention["parameter_constraints"][param_name] = {
                            "previous_value": previous_value,
                            "unconstrained_value": current_value,
                            "constrained_value": constrained_value
                        }
        
        return forgetting_prevention
    
    def adapt_learning_strategy(self, performance_feedback: Dict[str, Any]) -> AdaptationResult:
        """
        Adapt learning strategy based on performance feedback
        """
        adaptation_id = str(uuid.uuid4())
        
        # Analyze current performance
        current_performance = performance_feedback.get("performance_score", 0.5)
        recent_performance = [p["performance"] for p in self.performance_history[-10:]]
        
        if recent_performance:
            performance_trend = np.mean(recent_performance)
            performance_variance = np.var(recent_performance)
        else:
            performance_trend = 0.5
            performance_variance = 0.1
        
        # Determine adaptation strategy
        adaptation_strategy = self.adaptation_strategy
        parameters_updated = []
        performance_improvement = 0.0
        
        if current_performance < 0.3:
            # Poor performance - increase learning rate
            old_lr = self.learning_config["learning_rate"]
            self.learning_config["learning_rate"] = min(old_lr * 1.5, 0.1)
            parameters_updated.append("learning_rate")
            adaptation_strategy = AdaptationStrategy.GRADIENT_BASED
            
        elif current_performance > 0.8:
            # Good performance - fine-tune
            old_lr = self.learning_config["learning_rate"]
            self.learning_config["learning_rate"] = max(old_lr * 0.9, 0.001)
            parameters_updated.append("learning_rate")
            adaptation_strategy = AdaptationStrategy.META_LEARNING
            
        elif performance_variance > 0.2:
            # High variance - switch to more stable strategy
            self.learning_config["adaptation_threshold"] *= 0.8
            parameters_updated.append("adaptation_threshold")
            adaptation_strategy = AdaptationStrategy.NEUROPLASTICITY
        
        # Calculate performance improvement estimate
        if recent_performance:
            performance_improvement = current_performance - np.mean(recent_performance[-5:])
        
        # Create adaptation result
        adaptation_result = AdaptationResult(
            adaptation_id=adaptation_id,
            strategy_used=adaptation_strategy,
            parameters_updated=parameters_updated,
            performance_improvement=performance_improvement,
            confidence=min(current_performance + 0.2, 1.0),
            metadata={
                "performance_trend": performance_trend,
                "performance_variance": performance_variance,
                "adaptation_reason": "performance_feedback"
            },
            timestamp=datetime.utcnow()
        )
        
        self.adaptation_history.append(adaptation_result)
        self.adaptation_strategy = adaptation_strategy
        
        logger.info(f"ANAL adapted learning strategy: {adaptation_strategy.value}")
        return adaptation_result
    
    def federated_learning_update(self, global_updates: Dict[str, Any]) -> Dict[str, Any]:
        """
        Apply federated learning updates from other nodes
        """
        federated_result = {
            "update_id": str(uuid.uuid4()),
            "parameters_updated": [],
            "aggregation_method": "federated_averaging",
            "local_contribution": {},
            "timestamp": datetime.utcnow().isoformat()
        }
        
        # Apply federated averaging
        for param_name, global_value in global_updates.items():
            if param_name in self.model_parameters["weights"]:
                local_value = self.model_parameters["weights"][param_name]
                
                # Weighted average (simplified)
                aggregation_weight = 0.3  # Weight for global update
                new_value = (1 - aggregation_weight) * local_value + aggregation_weight * global_value
                
                self.model_parameters["weights"][param_name] = new_value
                
                federated_result["parameters_updated"].append(param_name)
                federated_result["local_contribution"][param_name] = {
                    "local_value": local_value,
                    "global_value": global_value,
                    "new_value": new_value
                }
        
        self.federated_updates.append(federated_result)
        
        logger.info(f"ANAL applied federated learning update: {federated_result['update_id']}")
        return federated_result
    
    def _update_performance_tracking(self, experience: LearningExperience, 
                                   learning_result: Dict[str, Any]) -> None:
        """Update performance tracking metrics"""
        performance_entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "experience_id": experience.experience_id,
            "performance": learning_result.get("error", 0.5),  # Lower error = better performance
            "learning_type": learning_result.get("learning_type", "unknown"),
            "adaptation_applied": bool(learning_result.get("neuroplasticity")),
            "forgetting_prevention_active": bool(learning_result.get("forgetting_prevention"))
        }
        
        self.performance_history.append(performance_entry)
        
        # Maintain history size
        if len(self.performance_history) > 1000:
            self.performance_history = self.performance_history[-500:]  # Keep recent half
    
    def get_learning_status(self) -> Dict[str, Any]:
        """Get comprehensive learning status"""
        recent_performance = [p["performance"] for p in self.performance_history[-10:]]
        
        return {
            "node_id": self.node_id,
            "learning_id": self.learning_id,
            "current_mode": self.current_mode.value,
            "adaptation_strategy": self.adaptation_strategy.value,
            "learning_config": self.learning_config,
            "experience_buffer_size": len(self.experience_buffer),
            "neural_connections": len(self.neural_connections),
            "model_parameters_count": len(self.model_parameters["weights"]),
            "importance_weights_count": len(self.importance_weights),
            "performance_history_length": len(self.performance_history),
            "recent_average_performance": np.mean(recent_performance) if recent_performance else 0.0,
            "adaptation_history_length": len(self.adaptation_history),
            "federated_updates_received": len(self.federated_updates)
        }

