from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    """Return the dashboard homepage"""
    return render(request, "index.html")
    