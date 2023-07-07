from django.shortcuts import render, redirect
from hashlib import sha256
from .models import link

def shorten_url(original_url):
	sha_url = (sha256(original_url.encode()).hexdigest())
	return sha_url[0:8]

def index(request):
    if request.method == 'POST':
        original = request.POST['url']
        short_code = shorten_url(original)
        short_link = link(original=original, shortened=short_code)
        if not link.objects.filter(shortened=short_code).exists():
            short_link.save()
        return render(request, 'urlshortener/index.html', {'short_link': short_link})

    return render(request, 'urlshortener/index.html')

def redirect_url(request, shortened):
    redirect_link = link.objects.get(shortened=shortened)
    return redirect(redirect_link.original)