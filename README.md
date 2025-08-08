## Math Microservice API

A production-ready FastAPI-based microservice for solving mathematical operations:

* Power (`pow`)
* Fibonacci (`n-th number`)
* Factorial

Features include:

* REST API (FastAPI)
* Database persistence (SQLite via SQLAlchemy)
* Caching (Fibonacci using `lru_cache`)
* Kafka logging
* Docker and Docker Compose support

## Functionality

### Supported Operations

| Operation   | Description                           | Input Fields        |
| ----------- | ------------------------------------- | ------------------- |
| `power`     | Computes `number` raised to `exp` | `number`, `exp` |
| `factorial` | Computes factorial of `number`        | `number`            |
| `fibonacci` | Computes the `n-th` Fibonacci number  | `number`            |

---

## Installation

### Run with Docker Compose

```bash
docker-compose up --build
```

Services:

* FastAPI: `http://localhost:8000`
* Kafka: `localhost:9092`

---

## API Usage

### Endpoint: `POST /api/calculate`

**Request Body:**

```json
{
  "operation": "power",
  "number": 2,
  "exp": 3
}
```

**Response:**

```json
{
  "result": 8
}
```

Other valid operations:

* `"factorial"` (needs `number`)
* `"fibonacci"` (needs `number`)

Use Swagger UI at [http://localhost:8000/docs](http://localhost:8000/docs)

---

## Viewing the SQLite Database

### Running in Docker

```bash
docker exec -it math-service /bin/sh
apk add sqlite
sqlite3 math.db
.tables
SELECT * FROM math_requests;
```

## Viewing Kafka Messages

### 1. Open Kafka shell

```bash
docker exec -it kafka /bin/bash
```

### 2. Start consumer:

```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic math_logs --from-beginning
```

You will see log messages like:

```json
{"operation": "fibonacci", "input": {"number": 6}, "result": 8}
```

---

## Key Packages

| Package                             | Purpose        |
| ----------------------------------- | -------------- |
| `fastapi`                           | API framework  |
| `uvicorn`                           | ASGI server    |
| `sqlalchemy`                        | ORM for SQLite |
| `kafka-python`                      | Kafka logging  |
| `functools`                         | Caching        |
| `pydantic`                          | Data validation and parsing |


---

## Project Structure

```
math_service
├── routers
│   └── api.py
├── services
│   ├── math_service.py
│   └── kafka_logger.py
├── utils
│   └── cache.py
├── database.py
├── docker-compose.yml
├── Dockerfile
├── main.py
├── models.py
├── README.md
└── requirements.txt
```

---

## Author

Andreea-Marina Son
