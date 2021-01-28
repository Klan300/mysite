from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Form
from .forms import CommentForm


def index(request):
    template_name = 'index.html'
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)

            new_comment.save()

            return redirect('index')
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'comment_form': comment_form})
