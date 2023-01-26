from django.shortcuts import render, redirect
from myApp.models import URL
import random
import string
from django.views.generic.base import RedirectView
# Create your views here.

def create_short_url(request):
    shortened_url = None
    if request.method == "POST":
        original_url = request.POST.get("original_url")
        shortened_url = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
        url = URL(original_url=original_url, shortened_url=shortened_url)
        url.save()
    return render(request, 'create_url.html', {'shortened_url': shortened_url})


def redirect_url(request, shortenedd):
    url = URL.objects.get(shortened_url=shortenedd)
    return RedirectView.as_view(url=url.original_url, permanent=True)(request)