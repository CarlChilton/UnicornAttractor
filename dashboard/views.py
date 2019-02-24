from django.shortcuts import render
from django.core import serializers
from bugs.models import Bug
from features.models import Feature
from django.http import JsonResponse, HttpResponse
import json
from django.db import connections
from django.db.models import Count

# Create your views here.
def index(request):
    """Return the dashboard homepage"""
    bugs = Bug.objects.order_by('-completed_date')
    features = Feature.objects.order_by('-completed_date')
    return render(request, "index.html", {"bugs": bugs, "features": features})
    
def bugsByMonth(request):
    bugs = serializers.serialize("json", Bug.objects.all())
    bugs = str(bugs)
    return HttpResponse(bugs, content_type="application/json")
    
def featuresByMonth(request):
    features = serializers.serialize("json", Feature.objects.all())
    features = str(features)
    return HttpResponse(features, content_type="application/json")
