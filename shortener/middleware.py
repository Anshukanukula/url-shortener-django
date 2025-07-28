import logging
from datetime import datetime

class LoggingMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print(f"[{datetime.now()}] {request.method} {request.get_full_path()}")
        return self.get_response(request)
