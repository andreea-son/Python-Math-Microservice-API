from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from database import Base

class MathRequest(Base):
    __tablename__ = "math_requests"

    id = Column(Integer, primary_key=True, index=True)
    operation = Column(String, index=True)
    input = Column(String)
    result = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)