from flask import Blueprint, request, jsonify
from datetime import datetime
import json
import uuid
from typing import Dict, List, Any

# Import core components
from src.core.echo_node_agent import EchoNodeAgent, LearningExperience
from src.core.daedalus_coordinator import DaedalusCoordinator, EvolutionDirective
from src.core.ppsds import PrivacyPreservingSyntheticDataSystem, SyntheticDataRequest, DataSchema, DataType, PrivacyLevel
from src.core.anal import NeuroAdaptiveLearning, LearningExperience as ANALExperience, AdaptationStrategy
from src.core.infinigen_engine import InfiniGenEngine, EvolutionDirective as InfiniGenDirective, EvolutionType
from src.core.cross_domain_intelligence import CrossDomainIntelligenceLayer, ContextType

# Import models
from src.models.echo_node import EchoNode, db
from src.models.task import Task, Goal

# Create blueprint
neur1genesis_bp = Blueprint('neur1genesis', __name__)

# Global instances (in production, these would be managed differently)
coordinator = DaedalusCoordinator()
ppsds = PrivacyPreservingSyntheticDataSystem()
cross_domain_layer = CrossDomainIntelligenceLayer()
echo_node_agents = {}  # Store active EchoNode agents
anal_modules = {}  # Store ANAL modules for each EchoNode
infinigen_engines = {}  # Store InfiniGen engines for each EchoNode

@neur1genesis_bp.route('/api/system/status', methods=['GET'])
def get_system_status():
    """Get overall system status"""
    try:
        status = {
            "system_id": "neur1genesis_v1",
            "timestamp": datetime.utcnow().isoformat(),
            "coordinator_status": coordinator.get_system_status(),
            "ppsds_status": ppsds.get_system_status(),
            "cross_domain_layer_status": cross_domain_layer.get_layer_status(),
            "active_echo_nodes": len(echo_node_agents),
            "active_anal_modules": len(anal_modules),
            "active_infinigen_engines": len(infinigen_engines),
            "database_echo_nodes": EchoNode.query.count(),
            "database_tasks": Task.query.count(),
            "database_goals": Goal.query.count()
        }
        
        return jsonify({"success": True, "data": status}), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# EchoNode Management Endpoints

@neur1genesis_bp.route('/api/echonodes', methods=['POST'])
def create_echo_node():
    """Create a new EchoNode"""
    try:
        data = request.get_json()
        
        # Create database entry
        echo_node = EchoNode()
        echo_node.status = 'idle'
        
        db.session.add(echo_node)
        db.session.commit()
        
        # Create agent instance
        agent = EchoNodeAgent(echo_node.id)
        echo_node_agents[echo_node.id] = agent
        
        # Create ANAL module
        anal_module = NeuroAdaptiveLearning(echo_node.id)
        anal_modules[echo_node.id] = anal_module
        
        # Create InfiniGen engine
        infinigen_engine = InfiniGenEngine(echo_node.id)
        infinigen_engines[echo_node.id] = infinigen_engine
        
        # Register with coordinator
        capabilities = data.get('capabilities', ['general_processing'])
        coordinator.register_echo_node(echo_node.id, capabilities)
        
        return jsonify({
            "success": True, 
            "data": {
                "echo_node_id": echo_node.id,
                "status": echo_node.status,
                "capabilities": capabilities,
                "created_at": echo_node.created_at.isoformat()
            }
        }), 201
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>', methods=['GET'])
def get_echo_node(echo_node_id):
    """Get EchoNode details"""
    try:
        # Get from database
        echo_node = EchoNode.query.get_or_404(echo_node_id)
        
        # Get agent status if active
        agent_status = None
        if echo_node_id in echo_node_agents:
            agent_status = echo_node_agents[echo_node_id].get_status_report()
        
        # Get ANAL status if active
        anal_status = None
        if echo_node_id in anal_modules:
            anal_status = anal_modules[echo_node_id].get_learning_status()
        
        # Get InfiniGen status if active
        infinigen_status = None
        if echo_node_id in infinigen_engines:
            infinigen_status = infinigen_engines[echo_node_id].get_engine_status()
        
        return jsonify({
            "success": True,
            "data": {
                "database_info": echo_node.to_dict(),
                "agent_status": agent_status,
                "anal_status": anal_status,
                "infinigen_status": infinigen_status
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>/perceive', methods=['POST'])
def echo_node_perceive(echo_node_id):
    """Make EchoNode perceive environmental data"""
    try:
        data = request.get_json()
        environmental_data = data.get('environmental_data', {})
        source = data.get('source', 'api')
        
        if echo_node_id not in echo_node_agents:
            return jsonify({"success": False, "error": "EchoNode agent not found"}), 404
        
        agent = echo_node_agents[echo_node_id]
        agent.perceive(environmental_data, source)
        
        return jsonify({
            "success": True,
            "data": {
                "message": "Perception completed",
                "echo_node_id": echo_node_id,
                "data_processed": len(str(environmental_data))
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>/execute_action', methods=['POST'])
def echo_node_execute_action(echo_node_id):
    """Execute action on EchoNode"""
    try:
        data = request.get_json()
        action = data.get('action', {})
        
        if echo_node_id not in echo_node_agents:
            return jsonify({"success": False, "error": "EchoNode agent not found"}), 404
        
        agent = echo_node_agents[echo_node_id]
        result = agent.execute_action(action)
        
        return jsonify({
            "success": True,
            "data": result
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>/empathy_assessment', methods=['POST'])
def echo_node_empathy_assessment(echo_node_id):
    """Perform contextual empathy assessment"""
    try:
        data = request.get_json()
        context = data.get('context', {})
        
        if echo_node_id not in echo_node_agents:
            return jsonify({"success": False, "error": "EchoNode agent not found"}), 404
        
        agent = echo_node_agents[echo_node_id]
        assessment = agent.contextual_empathy_assessment(context)
        
        return jsonify({
            "success": True,
            "data": assessment
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Daedalus Coordinator Endpoints

@neur1genesis_bp.route('/api/coordinator/goals', methods=['POST'])
def create_goal():
    """Create a new goal and parse it"""
    try:
        data = request.get_json()
        natural_language_input = data.get('natural_language_input', '')
        
        if not natural_language_input:
            return jsonify({"success": False, "error": "Natural language input required"}), 400
        
        # Parse goal using coordinator
        parsed_goal = coordinator.parse_natural_language_goal(natural_language_input)
        
        # Create database entry
        goal = Goal(
            id=parsed_goal['goal_id'],
            description=parsed_goal.get('parsed_objectives', [{}])[0] if parsed_goal.get('parsed_objectives') else 'Parsed goal',
            natural_language_input=natural_language_input,
            status='active'
        )
        
        db.session.add(goal)
        db.session.commit()
        
        # Decompose into tasks
        tasks = coordinator.decompose_goal_to_tasks(parsed_goal)
        
        # Create task database entries
        for task_data in tasks:
            task = Task(
                id=task_data['task_id'],
                goal_id=goal.id,
                description=task_data['description'],
                priority=task_data['priority'],
                status='pending'
            )
            db.session.add(task)
        
        db.session.commit()
        
        return jsonify({
            "success": True,
            "data": {
                "goal": goal.to_dict(),
                "parsed_goal": parsed_goal,
                "tasks_created": len(tasks)
            }
        }), 201
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/coordinator/tasks/<task_id>/allocate', methods=['POST'])
def allocate_task(task_id):
    """Allocate task to an EchoNode"""
    try:
        # Get task from database
        task = Task.query.get_or_404(task_id)
        
        if task.status != 'pending':
            return jsonify({"success": False, "error": "Task is not pending"}), 400
        
        # Convert to coordinator format
        task_data = {
            "task_id": task.id,
            "description": task.description,
            "required_capabilities": ["general_processing"],  # Simplified
            "priority": task.priority
        }
        
        # Allocate using coordinator
        selected_node = coordinator.consensus_driven_task_allocation(task_data)
        
        if selected_node:
            # Update database
            task.assign_to_echo_node(selected_node)
            db.session.commit()
            
            return jsonify({
                "success": True,
                "data": {
                    "task_id": task_id,
                    "assigned_to": selected_node,
                    "allocation_method": "consensus_driven"
                }
            }), 200
        else:
            return jsonify({"success": False, "error": "No suitable EchoNode available"}), 503
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/coordinator/meta_reflection', methods=['POST'])
def perform_meta_reflection():
    """Perform meta-reflection on system performance"""
    try:
        reflection_report = coordinator.meta_reflection()
        
        return jsonify({
            "success": True,
            "data": reflection_report
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/coordinator/federated_learning', methods=['POST'])
def coordinate_federated_learning():
    """Coordinate federated learning across EchoNodes"""
    try:
        data = request.get_json()
        learning_data = data.get('learning_data', {})
        
        learning_round = coordinator.coordinate_federated_learning(learning_data)
        
        return jsonify({
            "success": True,
            "data": learning_round
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# PPSDS Endpoints

@neur1genesis_bp.route('/api/ppsds/ingest', methods=['POST'])
def ingest_sensitive_data():
    """Ingest sensitive data for anonymization"""
    try:
        data = request.get_json()
        raw_data = data.get('raw_data', [])
        schema_data = data.get('schema', [])
        source_id = data.get('source_id', 'api_client')
        
        # Convert schema data to DataSchema objects
        schema = []
        for s in schema_data:
            data_schema = DataSchema(
                field_name=s['field_name'],
                data_type=DataType(s['data_type']),
                privacy_level=PrivacyLevel(s['privacy_level']),
                constraints=s.get('constraints', {}),
                metadata=s.get('metadata', {})
            )
            schema.append(data_schema)
        
        # Ingest data
        dataset_id = ppsds.ingest_sensitive_data(raw_data, schema, source_id)
        
        return jsonify({
            "success": True,
            "data": {
                "dataset_id": dataset_id,
                "records_processed": len(raw_data),
                "source_id": source_id
            }
        }), 201
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/ppsds/synthetic_data', methods=['POST'])
def generate_synthetic_data():
    """Generate synthetic data"""
    try:
        data = request.get_json()
        
        # Create schema
        schema_data = data.get('schema', [])
        schema = []
        for s in schema_data:
            data_schema = DataSchema(
                field_name=s['field_name'],
                data_type=DataType(s['data_type']),
                privacy_level=PrivacyLevel(s['privacy_level']),
                constraints=s.get('constraints', {}),
                metadata=s.get('metadata', {})
            )
            schema.append(data_schema)
        
        # Create request
        request_obj = SyntheticDataRequest(
            request_id=str(uuid.uuid4()),
            schema=schema,
            num_samples=data.get('num_samples', 100),
            privacy_budget=data.get('privacy_budget', 1.0),
            quality_requirements=data.get('quality_requirements', {}),
            timestamp=datetime.utcnow()
        )
        
        # Generate synthetic data
        response = ppsds.generate_synthetic_data(request_obj)
        
        return jsonify({
            "success": True,
            "data": {
                "request_id": response.request_id,
                "synthetic_data": response.synthetic_data,
                "quality_metrics": response.quality_metrics,
                "privacy_guarantees": response.privacy_guarantees,
                "generation_metadata": response.generation_metadata
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# ANAL Endpoints

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>/anal/learn', methods=['POST'])
def anal_learn_from_experience(echo_node_id):
    """Make ANAL module learn from experience"""
    try:
        data = request.get_json()
        
        if echo_node_id not in anal_modules:
            return jsonify({"success": False, "error": "ANAL module not found"}), 404
        
        # Create learning experience
        experience = ANALExperience(
            experience_id=str(uuid.uuid4()),
            input_data=data.get('input_data', {}),
            expected_output=data.get('expected_output'),
            actual_output=data.get('actual_output', {}),
            reward=data.get('reward'),
            context=data.get('context', {}),
            timestamp=datetime.utcnow()
        )
        
        # Learn from experience
        anal_module = anal_modules[echo_node_id]
        learning_result = anal_module.learn_from_experience(experience)
        
        return jsonify({
            "success": True,
            "data": learning_result
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>/anal/adapt', methods=['POST'])
def anal_adapt_learning_strategy(echo_node_id):
    """Adapt ANAL learning strategy"""
    try:
        data = request.get_json()
        performance_feedback = data.get('performance_feedback', {})
        
        if echo_node_id not in anal_modules:
            return jsonify({"success": False, "error": "ANAL module not found"}), 404
        
        anal_module = anal_modules[echo_node_id]
        adaptation_result = anal_module.adapt_learning_strategy(performance_feedback)
        
        return jsonify({
            "success": True,
            "data": {
                "adaptation_id": adaptation_result.adaptation_id,
                "strategy_used": adaptation_result.strategy_used.value,
                "parameters_updated": adaptation_result.parameters_updated,
                "performance_improvement": adaptation_result.performance_improvement,
                "confidence": adaptation_result.confidence,
                "metadata": adaptation_result.metadata
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# InfiniGen Endpoints

@neur1genesis_bp.route('/api/echonodes/<echo_node_id>/infinigen/evolve', methods=['POST'])
def infinigen_evolve_code(echo_node_id):
    """Evolve EchoNode code using InfiniGen"""
    try:
        data = request.get_json()
        
        if echo_node_id not in infinigen_engines:
            return jsonify({"success": False, "error": "InfiniGen engine not found"}), 404
        
        # Create evolution directive
        directive = InfiniGenDirective(
            directive_id=str(uuid.uuid4()),
            evolution_type=EvolutionType(data.get('evolution_type', 'optimize_performance')),
            target_modules=data.get('target_modules', []),
            parameters=data.get('parameters', {}),
            constraints=data.get('constraints', {}),
            expected_improvements=data.get('expected_improvements', {}),
            timestamp=datetime.utcnow()
        )
        
        # Evolve code
        infinigen_engine = infinigen_engines[echo_node_id]
        evolution_result = infinigen_engine.evolve_code(directive)
        
        return jsonify({
            "success": True,
            "data": {
                "result_id": evolution_result.result_id,
                "directive_id": evolution_result.directive_id,
                "success": evolution_result.success,
                "changes_made": evolution_result.changes_made,
                "new_modules": evolution_result.new_modules,
                "modified_modules": evolution_result.modified_modules,
                "performance_impact": evolution_result.performance_impact
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Cross-Domain Intelligence Layer Endpoints

@neur1genesis_bp.route('/api/cross_domain/ethical_inference', methods=['POST'])
def perform_ethical_inference():
    """Perform ethical inference"""
    try:
        data = request.get_json()
        decision_context = data.get('decision_context', {})
        
        inference_result = cross_domain_layer.ethical_inference(decision_context)
        
        return jsonify({
            "success": True,
            "data": inference_result
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/cross_domain/concept_fusion', methods=['POST'])
def perform_concept_fusion():
    """Perform analogy-driven concept fusion"""
    try:
        data = request.get_json()
        source_domain = data.get('source_domain', '')
        target_domain = data.get('target_domain', '')
        query_concept = data.get('query_concept', '')
        
        if not all([source_domain, target_domain, query_concept]):
            return jsonify({"success": False, "error": "Missing required parameters"}), 400
        
        fusion_result = cross_domain_layer.analogy_driven_concept_fusion(
            source_domain, target_domain, query_concept
        )
        
        return jsonify({
            "success": True,
            "data": fusion_result
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/cross_domain/cascade_intention', methods=['POST'])
def cascade_intention():
    """Cascade intention through the system"""
    try:
        data = request.get_json()
        original_intention = data.get('original_intention', '')
        context = data.get('context', {})
        stakeholders = data.get('stakeholders', [])
        
        if not original_intention:
            return jsonify({"success": False, "error": "Original intention required"}), 400
        
        cascade_result = cross_domain_layer.cascade_intention(
            original_intention, context, stakeholders
        )
        
        return jsonify({
            "success": True,
            "data": {
                "cascade_id": cascade_result.cascade_id,
                "original_intention": cascade_result.original_intention,
                "cascaded_intentions": cascade_result.cascaded_intentions,
                "context_adaptations": cascade_result.context_adaptations,
                "stakeholders": cascade_result.stakeholders,
                "ethical_considerations": cascade_result.ethical_considerations
            }
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Database Query Endpoints

@neur1genesis_bp.route('/api/echonodes', methods=['GET'])
def list_echo_nodes():
    """List all EchoNodes"""
    try:
        echo_nodes = EchoNode.query.all()
        return jsonify({
            "success": True,
            "data": [node.to_dict() for node in echo_nodes]
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/goals', methods=['GET'])
def list_goals():
    """List all goals"""
    try:
        goals = Goal.query.all()
        return jsonify({
            "success": True,
            "data": [goal.to_dict() for goal in goals]
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

@neur1genesis_bp.route('/api/tasks', methods=['GET'])
def list_tasks():
    """List all tasks"""
    try:
        tasks = Task.query.all()
        return jsonify({
            "success": True,
            "data": [task.to_dict() for task in tasks]
        }), 200
        
    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

# Health Check Endpoint
@neur1genesis_bp.route('/api/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "success": True,
        "data": {
            "status": "healthy",
            "timestamp": datetime.utcnow().isoformat(),
            "version": "1.0.0"
        }
    }), 200

