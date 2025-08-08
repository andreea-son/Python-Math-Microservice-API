from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from sqlalchemy.orm import Session
from database import SessionLocal
from models import MathRequest
from services.math_service import MathService
from services.kafka_logger import KafkaLogger

router = APIRouter(prefix="/api", tags=["math"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class MathPayload(BaseModel):
    operation: str
    number: int
    exp: int = None

@router.post("/calculate")
def calculate(payload: MathPayload, db: Session = Depends(get_db)):
    svc = MathService()
    op = payload.operation.lower()

    try:
        if op == "factorial":
            result = svc.compute_factorial(payload.number)
        elif op == "fibonacci":
            result = svc.compute_fibonacci(payload.number)
        elif op == "power":
            if payload.exp is None:
                raise ValueError("Exponent (exp) is required for power")
            result = svc.compute_power(payload.number, payload.exp)
        else:
            raise ValueError("Unsupported operation")
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    # save to database
    math_record = MathRequest(operation=op, input=str(payload.dict()), result=str(result))
    db.add(math_record)
    db.commit()

    # Kafka log
    kafka_logger = KafkaLogger(topic="math_logs")

    kafka_logger.log_event({
        "operation": op,
        "input": payload.dict(),
        "result": result
    })

    return {"result": result}
