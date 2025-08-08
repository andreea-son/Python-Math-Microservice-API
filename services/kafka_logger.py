import json
from kafka import KafkaProducer
from kafka.errors import KafkaError
from typing import Any, Dict
import logging

class KafkaLogger:
    def __init__(self, topic: str, bootstrap_servers: str = "kafka:9092"):
        self.topic = topic
        self.logger = logging.getLogger("KafkaLogger")

        try:
            self.producer = KafkaProducer(
                bootstrap_servers=bootstrap_servers,
                value_serializer=lambda v: json.dumps(v).encode("utf-8"),
                retries=3,
                acks="all",
            )
            self.logger.info("Kafka producer initialized successfully.")
        except Exception as e:
            self.producer = None
            self.logger.error(f"Failed to initialize Kafka producer: {e}")

    def log_event(self, message: Dict[str, Any]) -> bool:
        if not self.producer:
            self.logger.warning("Kafka producer is not initialized.")
            return False

        try:
            future = self.producer.send(self.topic, message)
            result = future.get(timeout=10)
            self.logger.info(f"Message sent to Kafka topic {self.topic}: {message}")
            return True
        except KafkaError as e:
            self.logger.error(f"Kafka error: {e}")
            return False
        except Exception as ex:
            self.logger.error(f"Unknown error sending Kafka message: {ex}")
            return False
