import uuid
from sqlalchemy import TIMESTAMP, Column, Integer, String, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import func
from ..init import Base

class Task(Base):
    __tablename__ = 'tasks'
    id = Column(Integer, primary_key=True)
    uuidtask = Column(UUID(as_uuid=True), unique=True, nullable=False, default=uuid.uuid4)
    username = Column(String(80), nullable=False)
    title = Column(String(120), nullable=False)
    description = Column(String(250))
    color = Column(String(10))
    active = Column(Boolean, default=True)
    preference = Column(Integer, default=1)
    created_at = Column(TIMESTAMP, server_default=func.now())
    updated_at = Column(TIMESTAMP, server_default=func.now())

    def to_dict(self):
        return {
            'uuidTask': str(self.uuidtask),
            'userName': self.username,
            'title': self.title,
            'description': self.description,
            'color': self.color,
            'active': self.active,
            'preference': self.preference,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }