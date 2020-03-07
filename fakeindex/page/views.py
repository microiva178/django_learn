from django.shortcuts import render
from .forms import testform

def page(request):
    if request.method == "POST":
        form = testform(request.POST)
        if form.is_valid():
            post = form.save(commit = False)
            post.save()
    else:
        form = testform()
    return render(request, 'page/page.html', {'form': form})