import json
import uuid
import logging
import re
from datetime import datetime
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict
from enum import Enum

from src.core.echo_node_agent import EchoNodeAgent

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class CoordinatorStatus(Enum):
    IDLE = "idle"
    PROCESSING = "processing"
    COORDINATING = "coordinating"
    META_REFLECTING = "meta_reflecting"

@dataclass
class TaskAllocation:
    """Represents a task allocation decision"""
    task_id: str
    echo_node_id: str
    confidence: float
    reasoning: str
    timestamp: datetime

@dataclass
class ConsensusDecision:
    """Represents a consensus decision among EchoNodes"""
    decision_id: str
    participants: List[str]
    decision_type: str
    outcome: Dict[str, Any]
    confidence: float
    timestamp: datetime

class DaedalusCoordinator:
    """
    Daedalus Coordinator - Dynamic orchestration of EchoNodes
    Handles natural language goal parsing, consensus-driven task allocation,
    meta-reflection, and federated learning coordination.
    """
    
    def __init__(self, coordinator_id: str = None):
        self.coordinator_id = coordinator_id or str(uuid.uuid4())
        self.status = CoordinatorStatus.IDLE
        
        # Registry of active EchoNodes
        self.active_echo_nodes: Dict[str, Dict[str, Any]] = {}
        
        # Task management
        self.global_task_queue: List[Dict[str, Any]] = []
        self.task_allocations: Dict[str, TaskAllocation] = {}
        
        # Meta-learning and optimization
        self.meta_learning_config: Dict[str, Any] = {
            "learning_rate": 0.01,
            "optimization_frequency": 100,
            "consensus_threshold": 0.7,
            "performance_metrics": {}
        }
        
        # Consensus tracking
        self.consensus_decisions: Dict[str, ConsensusDecision] = {}
        
        # Federated learning coordination
        self.federated_learning_rounds: List[Dict[str, Any]] = []
        
        logger.info(f"Daedalus Coordinator {self.coordinator_id} initialized")
    
    def register_echo_node(self, echo_node_id: str, capabilities: List[str] = None) -> bool:
        """
        Register an EchoNode with the coordinator
        """
        self.active_echo_nodes[echo_node_id] = {
            "echo_node_id": echo_node_id,
            "last_heartbeat": datetime.utcnow(),
            "current_load": 0.0,
            "capabilities": capabilities or [],
            "performance_history": [],
            "status": "idle"
        }
        
        logger.info(f"EchoNode {echo_node_id} registered with Daedalus Coordinator")
        return True
    
    def parse_natural_language_goal(self, natural_language_input: str) -> Dict[str, Any]:
        """
        Parse natural language goals into structured format
        """
        self.status = CoordinatorStatus.PROCESSING
        
        # Simple NLP parsing (in production, would use advanced NLP models)
        parsed_goal = {
            "goal_id": str(uuid.uuid4()),
            "original_input": natural_language_input,
            "parsed_objectives": [],
            "constraints": [],
            "priority": 1,
            "estimated_complexity": "medium",
            "required_capabilities": []
        }
        
        # Extract objectives using simple keyword matching
        objective_keywords = ["create", "build", "design", "implement", "develop", "generate", "analyze"]
        for keyword in objective_keywords:
            if keyword in natural_language_input.lower():
                parsed_goal["parsed_objectives"].append(f"{keyword}_objective")
        
        # Extract constraints
        constraint_keywords = ["must", "should", "required", "ensure", "guarantee"]
        for keyword in constraint_keywords:
            if keyword in natural_language_input.lower():
                parsed_goal["constraints"].append(f"{keyword}_constraint")
        
        # Determine required capabilities based on content
        if "web" in natural_language_input.lower() or "frontend" in natural_language_input.lower():
            parsed_goal["required_capabilities"].append("web_development")
        if "ai" in natural_language_input.lower() or "machine learning" in natural_language_input.lower():
            parsed_goal["required_capabilities"].append("ai_ml")
        if "data" in natural_language_input.lower():
            parsed_goal["required_capabilities"].append("data_processing")
        
        # Estimate complexity
        word_count = len(natural_language_input.split())
        if word_count > 100:
            parsed_goal["estimated_complexity"] = "high"
        elif word_count > 50:
            parsed_goal["estimated_complexity"] = "medium"
        else:
            parsed_goal["estimated_complexity"] = "low"
        
        self.status = CoordinatorStatus.IDLE
        logger.info(f"Parsed natural language goal: {parsed_goal['goal_id']}")
        
        return parsed_goal
    
    def decompose_goal_to_tasks(self, parsed_goal: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        Decompose complex goals into manageable tasks
        """
        tasks = []
        goal_id = parsed_goal["goal_id"]
        
        # Create tasks based on objectives and complexity
        for i, objective in enumerate(parsed_goal["parsed_objectives"]):
            task = {
                "task_id": str(uuid.uuid4()),
                "goal_id": goal_id,
                "description": f"Execute {objective} for goal {goal_id}",
                "priority": parsed_goal["priority"],
                "required_capabilities": parsed_goal["required_capabilities"],
                "status": "pending",
                "created_at": datetime.utcnow(),
                "estimated_effort": self._estimate_task_effort(objective, parsed_goal["estimated_complexity"])
            }
            tasks.append(task)
        
        # Add tasks to global queue
        self.global_task_queue.extend(tasks)
        
        logger.info(f"Decomposed goal {goal_id} into {len(tasks)} tasks")
        return tasks
    
    def _estimate_task_effort(self, objective: str, complexity: str) -> int:
        """
        Estimate effort required for a task (in arbitrary units)
        """
        base_effort = {"low": 10, "medium": 25, "high": 50}
        objective_multiplier = {
            "create_objective": 1.5,
            "build_objective": 2.0,
            "design_objective": 1.2,
            "implement_objective": 2.5,
            "analyze_objective": 1.0
        }
        
        effort = base_effort.get(complexity, 25)
        multiplier = objective_multiplier.get(objective, 1.0)
        
        return int(effort * multiplier)
    
    def consensus_driven_task_allocation(self, task: Dict[str, Any]) -> Optional[str]:
        """
        Allocate tasks using consensus-driven approach
        """
        self.status = CoordinatorStatus.COORDINATING
        
        # Get available EchoNodes
        available_nodes = [
            node_id for node_id, node_data in self.active_echo_nodes.items()
            if node_data["current_load"] < 0.8 and node_data["status"] == "idle"
        ]
        
        if not available_nodes:
            logger.warning("No available EchoNodes for task allocation")
            return None
        
        # Simulate bidding process
        bids = {}
        for node_id in available_nodes:
            node_data = self.active_echo_nodes[node_id]
            
            # Calculate bid score based on capabilities and load
            capability_match = len(set(task["required_capabilities"]) & 
                                 set(node_data["capabilities"])) / max(len(task["required_capabilities"]), 1)
            load_factor = 1.0 - node_data["current_load"]
            performance_factor = self._get_node_performance_factor(node_id)
            
            bid_score = (capability_match * 0.5 + load_factor * 0.3 + performance_factor * 0.2)
            bids[node_id] = bid_score
        
        # Select best bidder
        if bids:
            selected_node = max(bids, key=bids.get)
            confidence = bids[selected_node]
            
            # Create task allocation
            allocation = TaskAllocation(
                task_id=task["task_id"],
                echo_node_id=selected_node,
                confidence=confidence,
                reasoning=f"Selected based on capability match and load balance (score: {confidence:.2f})",
                timestamp=datetime.utcnow()
            )
            
            self.task_allocations[task["task_id"]] = allocation
            
            # Update node load
            self.active_echo_nodes[selected_node]["current_load"] += 0.2
            self.active_echo_nodes[selected_node]["status"] = "assigned"
            
            logger.info(f"Task {task['task_id']} allocated to EchoNode {selected_node}")
            self.status = CoordinatorStatus.IDLE
            return selected_node
        
        self.status = CoordinatorStatus.IDLE
        return None
    
    def _get_node_performance_factor(self, node_id: str) -> float:
        """
        Calculate performance factor for an EchoNode based on history
        """
        node_data = self.active_echo_nodes.get(node_id, {})
        performance_history = node_data.get("performance_history", [])
        
        if not performance_history:
            return 0.5  # Default performance factor
        
        # Calculate average performance from recent history
        recent_performance = performance_history[-10:]  # Last 10 tasks
        return sum(recent_performance) / len(recent_performance)
    
    def facilitate_consensus(self, decision_type: str, participants: List[str], 
                           options: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Facilitate consensus decision-making among EchoNodes
        """
        decision_id = str(uuid.uuid4())
        
        # Simulate consensus process
        votes = {}
        for participant in participants:
            # Simulate voting based on node preferences
            node_data = self.active_echo_nodes.get(participant, {})
            vote_weight = 1.0 / len(participants)  # Equal weight for simplicity
            
            # Select preferred option (simplified)
            preferred_option = options[0] if options else {"option": "default"}
            votes[participant] = {
                "option": preferred_option,
                "weight": vote_weight,
                "reasoning": f"Node {participant} preference"
            }
        
        # Determine consensus outcome
        if len(votes) >= len(participants) * self.meta_learning_config["consensus_threshold"]:
            outcome = {
                "decision": options[0] if options else {"decision": "default"},
                "consensus_reached": True,
                "vote_summary": votes
            }
            confidence = 0.8
        else:
            outcome = {
                "decision": None,
                "consensus_reached": False,
                "vote_summary": votes
            }
            confidence = 0.3
        
        # Record consensus decision
        consensus_decision = ConsensusDecision(
            decision_id=decision_id,
            participants=participants,
            decision_type=decision_type,
            outcome=outcome,
            confidence=confidence,
            timestamp=datetime.utcnow()
        )
        
        self.consensus_decisions[decision_id] = consensus_decision
        
        logger.info(f"Consensus decision {decision_id} completed with confidence {confidence}")
        return outcome
    
    def meta_reflection(self) -> Dict[str, Any]:
        """
        Perform meta-reflection on system performance and optimization
        """
        self.status = CoordinatorStatus.META_REFLECTING
        
        reflection_report = {
            "reflection_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "system_metrics": {},
            "optimization_recommendations": [],
            "performance_insights": {}
        }
        
        # Analyze system metrics
        total_nodes = len(self.active_echo_nodes)
        active_tasks = len([t for t in self.global_task_queue if t["status"] == "assigned"])
        completed_tasks = len([t for t in self.global_task_queue if t["status"] == "completed"])
        
        reflection_report["system_metrics"] = {
            "total_echo_nodes": total_nodes,
            "active_tasks": active_tasks,
            "completed_tasks": completed_tasks,
            "task_completion_rate": completed_tasks / max(len(self.global_task_queue), 1),
            "average_node_load": sum(node["current_load"] for node in self.active_echo_nodes.values()) / max(total_nodes, 1)
        }
        
        # Generate optimization recommendations
        avg_load = reflection_report["system_metrics"]["average_node_load"]
        if avg_load > 0.8:
            reflection_report["optimization_recommendations"].append("Consider adding more EchoNodes to handle load")
        elif avg_load < 0.3:
            reflection_report["optimization_recommendations"].append("System is under-utilized, consider more complex tasks")
        
        if reflection_report["system_metrics"]["task_completion_rate"] < 0.7:
            reflection_report["optimization_recommendations"].append("Investigate task allocation efficiency")
        
        # Performance insights
        reflection_report["performance_insights"] = {
            "most_efficient_node": self._get_most_efficient_node(),
            "bottlenecks_identified": self._identify_bottlenecks(),
            "learning_progress": self._assess_learning_progress()
        }
        
        self.status = CoordinatorStatus.IDLE
        logger.info(f"Meta-reflection completed: {reflection_report['reflection_id']}")
        
        return reflection_report
    
    def _get_most_efficient_node(self) -> Optional[str]:
        """Identify the most efficient EchoNode"""
        if not self.active_echo_nodes:
            return None
        
        best_node = None
        best_performance = 0
        
        for node_id, node_data in self.active_echo_nodes.items():
            performance = self._get_node_performance_factor(node_id)
            if performance > best_performance:
                best_performance = performance
                best_node = node_id
        
        return best_node
    
    def _identify_bottlenecks(self) -> List[str]:
        """Identify system bottlenecks"""
        bottlenecks = []
        
        # Check for overloaded nodes
        overloaded_nodes = [
            node_id for node_id, node_data in self.active_echo_nodes.items()
            if node_data["current_load"] > 0.9
        ]
        
        if overloaded_nodes:
            bottlenecks.append(f"Overloaded nodes: {overloaded_nodes}")
        
        # Check for task queue buildup
        pending_tasks = len([t for t in self.global_task_queue if t["status"] == "pending"])
        if pending_tasks > 10:
            bottlenecks.append(f"Task queue buildup: {pending_tasks} pending tasks")
        
        return bottlenecks
    
    def _assess_learning_progress(self) -> Dict[str, Any]:
        """Assess overall learning progress of the system"""
        return {
            "federated_learning_rounds": len(self.federated_learning_rounds),
            "consensus_decisions_made": len(self.consensus_decisions),
            "successful_task_allocations": len(self.task_allocations),
            "meta_learning_iterations": self.meta_learning_config.get("iterations", 0)
        }
    
    def coordinate_federated_learning(self, learning_data: Dict[str, Any]) -> Dict[str, Any]:
        """
        Coordinate federated learning across EchoNodes
        """
        learning_round = {
            "round_id": str(uuid.uuid4()),
            "timestamp": datetime.utcnow().isoformat(),
            "participants": list(self.active_echo_nodes.keys()),
            "learning_data": learning_data,
            "aggregation_method": "federated_averaging",
            "status": "initiated"
        }
        
        # Simulate federated learning coordination
        aggregated_updates = {}
        for node_id in learning_round["participants"]:
            # Simulate receiving updates from each node
            node_update = {
                "node_id": node_id,
                "model_updates": {"param_1": 0.1, "param_2": 0.05},  # Simulated
                "data_samples": 100,  # Simulated
                "learning_metrics": {"accuracy": 0.85, "loss": 0.15}
            }
            aggregated_updates[node_id] = node_update
        
        learning_round["aggregated_updates"] = aggregated_updates
        learning_round["status"] = "completed"
        
        self.federated_learning_rounds.append(learning_round)
        
        logger.info(f"Federated learning round {learning_round['round_id']} completed")
        return learning_round
    
    def get_system_status(self) -> Dict[str, Any]:
        """
        Get comprehensive system status
        """
        return {
            "coordinator_id": self.coordinator_id,
            "status": self.status.value,
            "active_echo_nodes": len(self.active_echo_nodes),
            "total_tasks": len(self.global_task_queue),
            "pending_tasks": len([t for t in self.global_task_queue if t["status"] == "pending"]),
            "completed_tasks": len([t for t in self.global_task_queue if t["status"] == "completed"]),
            "consensus_decisions": len(self.consensus_decisions),
            "federated_learning_rounds": len(self.federated_learning_rounds),
            "meta_learning_config": self.meta_learning_config
        }


@dataclass
class EvolutionDirective:
    """Represents an evolution directive for system adaptation"""
    directive_id: str
    directive_type: str
    target_component: str
    parameters: Dict[str, Any]
    priority: int
    timestamp: datetime
    status: str  # pending, executing, completed, failed
    
    def __post_init__(self):
        if not self.directive_id:
            self.directive_id = str(uuid.uuid4())

