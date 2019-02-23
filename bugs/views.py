from django.shortcuts import render

# Create your views here.
def bugs(request):
    """Return the dashboard homepage"""
    return render(request, "bugs.html")
