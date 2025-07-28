# Django URL Shortener

A Django microservice to shorten URLs and redirect to the original URLs.

## 🔧 Endpoints

- `POST /shortener/create/` — Create a short URL  
- `GET /shortener/<short_code>/` — Redirect to the original URL  
- `GET /shortener/list/` — List all URLs in JSON

## 🚀 How to Run

```bash
# Install requirements
pip install -r requirements.txt

# Run the server
python manage.py runserver
