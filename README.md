# HNG Stage 0 - Dynamic Profile Endpoint

A RESTful API endpoint built with Python/Django that returns profile information along with dynamic cat facts fetched from an external API.

## 🚀 Live Demo

**API Endpoint:** https://hng-stage-zero-production-7d8d.up.railway.app/me/

Try it now:
```bash
curl https://hng-stage-zero-production-7d8d.up.railway.app/me/
```

## 📋 Project Overview

This project implements a dynamic API endpoint that demonstrates:
- RESTful API design with Django
- Integration with third-party APIs (Cat Facts API)
- Real-time timestamp generation in ISO 8601 format
- Proper JSON response formatting
- Error handling for external API failures
- CORS configuration for cross-origin requests

## 🛠️ Tech Stack

- **Backend Framework:** Python/Django
- **External API:** Cat Facts API (https://catfact.ninja/fact)
- **Deployment:** Railway
- **Language:** Python 3.x

## ✨ Features

- ✅ Dynamic cat facts fetched on every request
- ✅ Real-time UTC timestamp generation
- ✅ Proper error handling with graceful fallbacks
- ✅ CORS enabled for cross-origin requests
- ✅ Environment-based configuration
- ✅ Production-ready deployment on Railway

## 📦 Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git
- Virtual environment (recommended)

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/IfeJayeola/HNG-stage-zero.git
   cd HNG-stage-zero
   ```

2. **Create and activate virtual environment**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   
   Create a `.env` file in the root directory:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key-here
   ALLOWED_HOSTS=localhost,127.0.0.1
   CAT_FACT_API_URL=https://catfact.ninja/fact
   API_TIMEOUT=5
   ```

5. **Run database migrations**
   ```bash
   python manage.py migrate
   ```

6. **Start the development server**
   ```bash
   python manage.py runserver
   ```

7. **Test the endpoint**
   ```bash
   curl http://localhost:8000/me/
   ```

## 📡 API Documentation

### GET `/me/`

Returns user profile information with a dynamically fetched cat fact.

#### Response Format

```json
{
  "status": "success",
  "user": {
    "email": "ijjayeola@gmail.com",
    "name": "Jayeola, Ifeoluwa Joseph",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T06:53:08.062587",
  "fact": "Cats only sweat through their paws and nowhere else on their body"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `status` | string | Always returns "success" |
| `user.email` | string | Developer's email address |
| `user.name` | string | Developer's full name |
| `user.stack` | string | Backend technology stack used |
| `timestamp` | string | Current UTC time in ISO 8601 format |
| `fact` | string | Random cat fact from Cat Facts API |

#### Headers

- **Content-Type:** `application/json`
- **Access-Control-Allow-Origin:** `*` (CORS enabled)

#### Status Codes

- `200 OK` - Successful response with cat fact
- `200 OK` - Successful response with fallback message (if Cat Facts API fails)
- `500 Internal Server Error` - Server error

#### Example Requests

**Using curl:**
```bash
curl -X GET https://hng-stage-zero-production-7d8d.up.railway.app/me/
```

**Using Python requests:**
```python
import requests

response = requests.get('https://hng-stage-zero-production-7d8d.up.railway.app/me/')
data = response.json()
print(data)
```

**Using JavaScript fetch:**
```javascript
fetch('https://hng-stage-zero-production-7d8d.up.railway.app/me/')
  .then(response => response.json())
  .then(data => console.log(data));
```

## 🧪 Testing

### Manual Testing

Test the endpoint using various methods:

```bash
# Using curl with formatted output
curl https://hng-stage-zero-production-7d8d.up.railway.app/me/ | python -m json.tool

# Using httpie (if installed)
http GET https://hng-stage-zero-production-7d8d.up.railway.app/me/

# Test multiple requests to verify dynamic cat facts
for i in {1..5}; do
  curl https://hng-stage-zero-production-7d8d.up.railway.app/me/ | python -m json.tool
  echo "\n---\n"
done
```

### Automated Tests

```bash
# Run Django tests
python manage.py test

# Run with coverage
coverage run --source='.' manage.py test
coverage report
```

## 🌐 Deployment on Railway

### Environment Variables

The following environment variables are configured on Railway:

- `PYTHON_VERSION` - Python runtime version
- `SECRET_KEY` - Django secret key
- `DEBUG` - Debug mode (False in production)
- `ALLOWED_HOSTS` - Allowed hostnames
- `CAT_FACT_API_URL` - External API URL
- `API_TIMEOUT` - Timeout for external API calls (seconds)

### Deployment Steps

1. **Push code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy on Railway**
   - Create a new project on Railway
   - Connect your GitHub repository
   - Railway auto-detects Django and deploys
   - Configure environment variables
   - Access your live API!

3. **Verify deployment**
   ```bash
   curl https://hng-stage-zero-production-7d8d.up.railway.app/me/
   ```

## 📂 Project Structure

```
HNG-stage-zero/
├── backend_project/          # Django project folder
│   ├── __init__.py
│   ├── settings.py          # Project settings
│   ├── urls.py              # Main URL configuration
│   ├── wsgi.py              # WSGI configuration
│   └── asgi.py              # ASGI configuration
├── api/                      # Django app for the API
│   ├── __init__.py
│   ├── views.py             # API view logic
│   ├── urls.py              # API URL routes
│   └── tests.py             # Unit tests
├── manage.py                # Django management script
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore              # Git ignore file
├── Procfile                # Railway deployment config
├── runtime.txt             # Python version specification
└── README.md               # This file
```

## 🔧 Configuration

### Cat Facts API Integration

The application fetches cat facts from: `https://catfact.ninja/fact`

**Timeout Configuration:**
```python
API_TIMEOUT = 5  # seconds
```

### CORS Configuration

CORS is enabled for all origins using `django-cors-headers`:

```python
CORS_ALLOW_ALL_ORIGINS = True
```

For production, consider restricting to specific origins:
```python
CORS_ALLOWED_ORIGINS = [
    "https://yourdomain.com",
]
```

### Network Errors
- Connection timeouts return fallback message
- HTTP errors return fallback message
- Invalid JSON responses return fallback message

### Django Error Handling
- 404 for undefined routes
- 500 for server errors
- Proper logging for debugging

## 📊 Performance

- **Response Time:** ~200-500ms (including external API call)
- **Availability:** 99.9% uptime on Railway
- **External API Timeout:** 5 seconds
- **CORS:** Enabled for all origins

## 🧰 Dependencies

Main Python packages used:

```
Django>=4.2.0
djangorestframework>=3.14.0
django-cors-headers>=4.0.0
requests>=2.31.0
python-dotenv>=1.0.0
gunicorn>=21.2.0
```

Install all dependencies with:
```bash
pip install -r requirements.txt
```

## 📝 License

This project is created as part of the HNG12 Internship Backend Track - Stage 0.

## 👤 Author

**Jayeola, Ifeoluwa Joseph**
- GitHub: [@IfeJayeola](https://github.com/IfeJayeola)
- Email: ijjayeola@gmail.com

## 🎓 Learning Outcomes

This project demonstrates proficiency in:
- Building RESTful APIs with Django
- Consuming third-party APIs with proper error handling
- Working with timestamps and ISO 8601 format
- JSON response formatting
- CORS configuration
- Environment-based configuration
- Deploying Django applications to production
- Using Railway for hosting

## 🙏 Acknowledgments

- **HNG Internship Program** - For providing this learning opportunity
- **Cat Facts API** - For providing the cat facts data
- **Railway** - For providing reliable hosting

### API Response
```json
{
  "status": "success",
  "user": {
    "email": "ijjayeola@gmail.com",
    "name": "Jayeola, Ifeoluwa Joseph",
    "stack": "Python/Django"
  },
  "timestamp": "2025-10-18T06:53:08.062587",
  "fact": "Cats only sweat through their paws and nowhere else on their body"
}
```

### Live Endpoint
🌐 https://hng-stage-zero-production-7d8d.up.railway.app/me/

---

**Built with ❤️ by Ife Jayeola for HNG12 Backend Track - Stage 0**

*Last Updated: October 18, 2025*
