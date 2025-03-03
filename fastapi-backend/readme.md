# FastAPI Secure Address API 🚀

## 📌 Overview  
This is a **production-ready** FastAPI backend that exposes a secure **GET** endpoint (`/address`).  
- Supports **environment variables** (postcode from `.env`)  
- Includes **API key authentication** for security  
- Implements **rate limiting** to prevent abuse  
- Uses **logging** for monitoring  
- Supports **CORS** for frontend integration  

---

## ⚙️ Setup & Installation  

### ** Clone the Repository**  
```sh
git clone https://github.com/mdad-elec/fastapi-backend.git
cd fastapi-backend
pip install -r requirements.txt

create .env file and add:
POSTCODE=12345
API_KEY=supersecureapikey123

run fastapi app:
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload

fetch an address:
curl -X GET "http://127.0.0.1:8000/address" -H "X-API-KEY: supersecureapikey123"

🔒 Production Features
API Key Authentication: Requests must include a valid X-API-KEY.
Rate Limiting: Limits 5 requests per minute per user.
CORS Protection: Restricts access to approved domains.
Logging: All requests are logged for debugging and security.

🛠️ Future Enhancements
🔹 JWT Authentication for better security
🔹 Database Support (PostgreSQL, MongoDB)
🔹 Advanced Monitoring (Prometheus, Grafana)`
🔹 Ngnix for domain and adding ssl certificate 

## Production-grade deployment guides

1️⃣ FastAPI Official Documentation
✅ Best practices for structuring a FastAPI project
✅ Using Pydantic for request validation and response modeling
✅ Environment variables handling with dotenv
📌 Reference: FastAPI Documentation

2️⃣ Uvicorn & ASGI Deployment Best Practices
✅ Running FastAPI with Uvicorn for high-performance async handling
✅ Using gunicorn with multiple workers for production
📌 Reference: Uvicorn Docs

3️⃣ Logging Best Practices (loguru)
✅ Using loguru for structured logging instead of default logging
✅ Setting up file rotation for long-term logs
📌 Reference: Loguru GitHub

4️⃣ Security & API Key Authentication
✅ Using FastAPI's Depends() to secure endpoints
✅ Enforcing X-API-KEY headers for controlled access
📌 Reference: FastAPI Security Docs

5️⃣ Rate Limiting for API Protection (slowapi)
✅ Preventing abuse by adding request limits per user
✅ Using slowapi with ASGI middleware for seamless rate limiting
📌 Reference: SlowAPI GitHub

6️⃣ CORS & Frontend Security Considerations
✅ Restricting API access to specific frontend origins
✅ Ensuring API security while allowing controlled cross-origin access
📌 Reference: FastAPI CORS Middleware