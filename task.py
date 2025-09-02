from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import uuid

db = SQLAlchemy()

class Task(db.Model):
    __tablename__ = 'tasks'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    goal_id = db.Column(db.String(36), nullable=True)
    description = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='pending')  # pending, assigned, completed, failed
    assigned_to = db.Column(db.String(36), db.ForeignKey('echo_nodes.id'), nullable=True)
    priority = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)
    
    # Relationship to EchoNode
    echo_node = db.relationship('EchoNode', backref='assigned_tasks', foreign_keys=[assigned_to])
    
    def __repr__(self):
        return f'<Task {self.id}>'
    
    def to_dict(self):
        """Convert Task to dictionary"""
        return {
            'task_id': self.id,
            'goal_id': self.goal_id,
            'description': self.description,
            'status': self.status,
            'assigned_to': self.assigned_to,
            'priority': self.priority,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }
    
    def update_status(self, new_status):
        """Update task status"""
        valid_statuses = ['pending', 'assigned', 'completed', 'failed']
        if new_status in valid_statuses:
            self.status = new_status
            self.updated_at = datetime.utcnow()
            if new_status in ['completed', 'failed']:
                self.completed_at = datetime.utcnow()
        else:
            raise ValueError(f"Invalid status: {new_status}. Must be one of {valid_statuses}")
    
    def assign_to_echo_node(self, echo_node_id):
        """Assign task to an EchoNode"""
        self.assigned_to = echo_node_id
        self.status = 'assigned'
        self.updated_at = datetime.utcnow()


class Goal(db.Model):
    __tablename__ = 'goals'
    
    id = db.Column(db.String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    description = db.Column(db.Text, nullable=False)
    natural_language_input = db.Column(db.Text, nullable=False)
    status = db.Column(db.String(20), nullable=False, default='active')  # active, completed, failed, paused
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    
    # Relationship to Tasks
    tasks = db.relationship('Task', backref='goal', foreign_keys='Task.goal_id')
    
    def __repr__(self):
        return f'<Goal {self.id}>'
    
    def to_dict(self):
        """Convert Goal to dictionary"""
        return {
            'goal_id': self.id,
            'description': self.description,
            'natural_language_input': self.natural_language_input,
            'status': self.status,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat(),
            'tasks': [task.to_dict() for task in self.tasks]
        }

