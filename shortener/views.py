import string
import random
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.core.serializers import serialize
from .models import ShortURL


# Helper function to generate short code
def generate_short_code(length=6):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choices(characters, k=length))

# 1. HTML form page (index.html)
def index(request):
    short_url = None
    if request.method == 'POST':
        original_url = request.POST.get('original_url')
        short_code = generate_short_code()
        url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
        short_url = request.build_absolute_uri(f"/shortener/{short_code}/")
    return render(request, 'shortener/index.html', {'short_url': short_url})

# 2. API: Create short URL from JSON input
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def create_short_url(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        original_url = data.get('original_url')
        if not original_url:
            return JsonResponse({'error': 'original_url is required'}, status=400)
        short_code = generate_short_code()
        url = ShortURL.objects.create(original_url=original_url, short_code=short_code)
        return JsonResponse({'short_code': short_code})
    return JsonResponse({'error': 'POST method required'}, status=405)

# 3. Redirect view
def redirect_url(request, short_code):
    url = get_object_or_404(ShortURL, short_code=short_code)
    return HttpResponseRedirect(url.original_url)

# 4. List all URLs (JSON)
def list_all_urls(request):
    urls = ShortURL.objects.all()
    data = serialize('json', urls)
    return HttpResponse(data, content_type='application/json')
