from django.shortcuts import render

# Create your views here.
def features(request):
    """Return the dashboard homepage"""
    return render(request, "features.html")
