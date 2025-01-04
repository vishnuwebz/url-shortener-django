from django.shortcuts import render, redirect, get_object_or_404
from .models import ShortURL
import string, random

# Create your views here.

def shorten_url(request):
    if request.method == "POST":
        long_url = request.POST.get('url')
        short_code = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        new_url = ShortURL(original_url=long_url, short_code=short_code)
        new_url.save()
        return render(request, 'result.html', {'short_code': short_code})
    return render(request, 'index.html')

def redirect_url(request, short_code):
    short_url = get_object_or_404(ShortURL, short_code=short_code)
    return redirect(short_url.original_url)
