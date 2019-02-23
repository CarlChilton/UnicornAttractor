from django.shortcuts import render

# Create your views here.
def accounts(request):
    """Return the dashboard homepage"""
    return render(request, "accounts.html")
