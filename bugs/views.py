from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Bug
from .forms import AddBugForm

# Create your views here.
def bugs(request):
    bugs = Bug.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')
    return render(request, "bugs.html", {'bugs': bugs})

def bug_detail(request, pk):
    bug = get_object_or_404(Bug, pk=pk)
    bug.save()
    return render(request, "bugs.html", {'bug': bug})

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