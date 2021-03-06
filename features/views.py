from django.shortcuts import render, get_object_or_404, redirect, reverse
import os
from django.utils import timezone
from .models import Feature, Comment
from .forms import AddFeatureForm, AddFeatureCommentForm
from django.conf import settings
import stripe
import datetime

stripe.api_key = settings.STRIPE_SECRET_KEY.replace("'", "")

# Create your views here.
def features(request):
    features = Feature.objects.order_by('-upvotes')
    comments = Comment.objects.order_by('-created_date')
    return render(request, "features.html", {'features': features, 'comments': comments})
    
def upvote_feature(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    key = settings.STRIPE_PUBLISHABLE_KEY
    return render(request, "upvotefeature.html", {'key': key, 'feature': feature})
    
def payment(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.upvotes += 1
    feature.save()
    if request.method == 'POST':
        payment = stripe.Charge.create(
            amount=500,
            currency='gbp',
            description='Payment for a feature upvote',
            source=request.POST['stripeToken']
        )
        return render(request, 'payment.html', {'feature': feature})



def create_or_edit_feature(request, pk=None):
    feature = get_object_or_404(Feature, pk=pk) if pk else None
    if request.method == "POST":
        form = AddFeatureForm(request.POST, request.FILES, instance=feature)
        if form.is_valid():
            feature = form.save()
            return redirect(features)
    else:
        form = AddFeatureForm(instance=feature)
    return render(request, 'addfeature.html', {'form': form})
    
def add_comment(request, pk):
    form = AddFeatureCommentForm(request.POST)
    if request.method == "POST":
        form = AddFeatureCommentForm(request.POST)
        form.contents = request.POST.get('contents')
        form.user = request.POST.get('user')
        if form.is_valid():
            form.save()
            return redirect(reverse('features'))    
    return redirect(reverse('features'))

def mark_done_feature(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.status = request.POST.get("status")
    feature.completed_date = datetime.datetime.now()
    feature.save()
    return redirect(reverse('features'))
    
def mark_doing_feature(request, pk):
    feature = get_object_or_404(Feature, pk=pk)
    feature.status = request.POST.get("status")
    feature.save()
    return redirect(reverse('features'))