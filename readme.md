# HNG Stage Zero API

A Django REST Framework API that returns specific user information including email, current datetime, and GitHub repository URL.

## Description

This API is built using Django REST Framework and provides a single endpoint that returns:
- Registered email address
- Current datetime in ISO 8601 format
- GitHub repository URL

The API is built as part of the HNG Internship program requirements.

## Technologies Used

- Python 3.8+
- Django==5.1.5
- django-cors-headers==4.6.0
- djangorestframework==3.15.2

## Setup and Installation

### Prerequisites

- Python 3.8 or higher
- pip

### Local Development

1. Clone the repository
```bash
git clone https://github.com/baffa-m/hng12_backend
cd hng12_backend
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Run the development server
```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

## API Documentation

### Endpoint

- URL: `GET /`
- Description: Returns user information including email, current datetime, and GitHub URL

### Response Format

```json
{
  "email": "your-email@example.com",
  "current_datetime": "2025-01-30T09:30:00Z",
  "github_url": "<https://github.com/yourusername/your-repo>"
}
```

### Status Codes

- 200: Successful request
- 500: Server error

### Example Usage

Using curl:
```bash
curl https://baffam.pythonanywhere.com/task0
```

## Deployment

T PythonAnywhere




## Resources

Learn more about HNG Internship?, visit:
[HNG Python Developers](https://hng.tech/hire/python-developers)

