# API REST de Estudiantes (Python)

Proyecto en **Python + FastAPI** para gestionar estudiantes con CRUD básico.

## Requisitos

- Python 3.10+

## Instalación

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt -r test_requirements.txt
```

## Ejecutar la API

```bash
uvicorn main:app --reload
```

La API quedará en `http://127.0.0.1:8000`.
Documentación automática:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## Endpoints

- `GET /health`
- `GET /students`
- `POST /students`
- `GET /students/{student_id}`
- `PUT /students/{student_id}`
- `DELETE /students/{student_id}`

## Ejemplo rápido con cURL

```bash
curl -X POST http://127.0.0.1:8000/students \
  -H "Content-Type: application/json" \
  -d '{"name":"Ana Perez","age":20,"email":"ana@example.com"}'

curl http://127.0.0.1:8000/students
```

## Tests

```bash
pytest -q
```
