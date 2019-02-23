from django.shortcuts import render

# Create your views here.
def index(request):
    """Return the dashboard homepage"""
    return render(request, "index.html")
    