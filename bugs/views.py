from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.utils import timezone
from .models import Bug, Comment
from .forms import AddBugForm, AddBugCommentForm

# Create your views here.
def bugs(request):
    bugs = Bug.objects.order_by('-upvotes')
    comments = Comment.objects.order_by('-created_date')
    return render(request, "bugs.html", {'bugs': bugs, 'comments': comments})

def upvote_bug(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    bug.upvotes += 1
    bug.save()
    return redirect(reverse('bugs'))
    

def create_or_edit_bug(request, pk=None):
    """
    Create a view that allows us to create
    or edit a post depending if the Post ID
    is null or not
    """
    bug = get_object_or_404(Bug, pk=pk) if pk else None
    if request.method == "POST":
        form = AddBugForm(request.POST, request.FILES, instance=bug)
        if form.is_valid():
            bug = form.save()
            return redirect(bugs)
    else:
        form = AddBugForm(instance=bug)
    return render(request, 'addbug.html', {'form': form})
    
def add_comment(request, pk):
    form = AddBugCommentForm(request.POST)
    if request.method == "POST":
        form = AddBugCommentForm(request.POST)
        form.contents = request.POST.get('contents')
        form.user = request.POST.get('user')
        # form.bug_id = pk
        if form.is_valid():
            form.save()
            return redirect(reverse('bugs'))    
    return redirect(reverse('bugs'))
    
    
    
    