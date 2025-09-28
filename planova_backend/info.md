docker build -t return1101-api .

docker run -d -p 8002:8002 return1101-api

uvicorn app.main:app --host 0.0.0.0 --port 8000

python3 -m app.utils.create_tables

# ---> App API LOGIC
whois-fastapi-project/
├── app/
│   ├── main.py               # 1. FastAPI app instance + include routers
│   ├── api/
│   │   ├── __init__.py       # 2. Import and expose API routers here
│   │   └── whois.py          # 3. FastAPI endpoints for Whois API
│   ├── core/
│   │   ├── __init__.py       # 4. Core module initialization
│   │   ├── config.py         # 5. Configurations (e.g. env variables)
│   │   └── middleware.py     # 6. Middleware (logging, auth, CORS, etc)
│   ├── services/
│   │   ├── __init__.py       # 7. Service module initialization
│   │   └── whois_service.py  # 8. Business logic and Whois functionality
│   ├── models/
│   │   ├── __init__.py       # 9. Models module initialization
│   │   └── whois_models.py   # 10. Pydantic models (request/response schemas)
├── tests/
│   └── test_whois.py         # 11. Unit and integration tests for Whois
├── Dockerfile                # 12. Docker image build instructions
├── requirements.txt          # 13. Python dependencies
├── README.md                 # 14. Project documentation
├── info.md                   # 15. Additional notes/documentation


================================>
Front si back separat.
/whois-api/ (pentru front --- sa nu para ceva ciudat)
/whius-backend/ (sa pot diferentia)

curl -X POST http://0.0.0.0:8000/whois-backend/auth/register \
  -H "Content-Type: application/json" \
  -d '{
    "username": "example_123",
    "password": "parola123",
    "email": "andrei.reporter13@gmail.com"i
  }'


curl -H "Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJ1c2VyMSIsImV4cCI6MTc1MjI3NDM5M30.LtuFgpLK33BzYe2It9E-pGs-195R-GBdM4-pVuDrDt8" "http://localhost:8000/whois?domain=peviitor.com"
