from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post


# Create your views here.
def post_list(request, *args, **kwargs):

    messages.success(request, 'Welcome to powwow! We collect comments from news sites and share them in a single feed. Enjoy!')
    

    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')[0:100]
    
    return render(request, 'powwows/post_list.html', {'posts':posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'powwows/post_detail.html', {'post': post})


