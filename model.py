from sqlalchemy import Column, Integer, String, Text, DateTime, ForeignKey, TIMESTAMP
from db import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50),nullable=True)
    email = Column(String(100), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)

class Reports(Base):
    __tablename__ = "reports"
    
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    resume_text = Column(Text, nullable=False)
    report_text = Column(Text, nullable=False)
    created_at = Column(DateTime, nullable=True, default= TIMESTAMP)
