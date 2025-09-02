from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import json
import uuid

db = SQLAlchemy()

class EchoNode(db.Model):
    __tablename__ = 'echo_nodes'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    status = db.Column(db.String(20), nullable=False, default='idle')  # active, idle, learning, metaprogramming
    beliefs = db.Column(db.Text, nullable=False, default='{}')  # JSON string
    desires = db.Column(db.Text, nullable=False, default='[]')  # JSON string
    intentions = db.Column(db.Text, nullable=False, default='[]')  # JSON string
    learned_parameters = db.Column(db.Text, nullable=False, default='{}')  # JSON string
    code_version = db.Column(db.String(50), nullable=False, default='1.0.0')
    last_updated = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    def __repr__(self):
        return f'<EchoNode {self.id}>'
    
    def get_beliefs(self):
        """Parse beliefs JSON string to dictionary"""
        try:
            return json.loads(self.beliefs)
        except json.JSONDecodeError:
            return {}
    
    def set_beliefs(self, beliefs_dict):
        """Set beliefs from dictionary"""
        self.beliefs = json.dumps(beliefs_dict)
        self.last_updated = datetime.utcnow()
    
    def get_desires(self):
        """Parse desires JSON string to list"""
        try:
            return json.loads(self.desires)
        except json.JSONDecodeError:
            return []
    
    def set_desires(self, desires_list):
        """Set desires from list"""
        self.desires = json.dumps(desires_list)
        self.last_updated = datetime.utcnow()
    
    def get_intentions(self):
        """Parse intentions JSON string to list"""
        try:
            return json.loads(self.intentions)
        except json.JSONDecodeError:
            return []
    
    def set_intentions(self, intentions_list):
        """Set intentions from list"""
        self.intentions = json.dumps(intentions_list)
        self.last_updated = datetime.utcnow()
    
    def get_learned_parameters(self):
        """Parse learned parameters JSON string to dictionary"""
        try:
            return json.loads(self.learned_parameters)
        except json.JSONDecodeError:
            return {}
    
    def set_learned_parameters(self, params_dict):
        """Set learned parameters from dictionary"""
        self.learned_parameters = json.dumps(params_dict)
        self.last_updated = datetime.utcnow()
    
    def to_dict(self):
        """Convert EchoNode to dictionary"""
        return {
            'echo_node_id': self.id,
            'status': self.status,
            'beliefs': self.get_beliefs(),
            'desires': self.get_desires(),
            'intentions': self.get_intentions(),
            'learned_parameters': self.get_learned_parameters(),
            'code_version': self.code_version,
            'last_updated': self.last_updated.isoformat(),
            'created_at': self.created_at.isoformat()
        }
    
    def update_status(self, new_status):
        """Update EchoNode status"""
        valid_statuses = ['active', 'idle', 'learning', 'metaprogramming']
        if new_status in valid_statuses:
            self.status = new_status
            self.last_updated = datetime.utcnow()
        else:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}")

