from django.contrib import messages
from django.shortcuts import render, get_object_or_404

from django.utils import timezone
from .models import Post
from el_pagination.decorators import page_template

@page_template('powwows/post_list_page.html')
# Create your views here.
def post_list(request, template = 'powwows/post_list.html', extra_context = None, *args, **kwargs):

    messages.success(request, 'Welcome to powwow! We collect comments from news stories and share them in a single feed. Enjoy!')
    
    context={
    'posts':Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    
    }
    if extra_context is not None:
    	context.update(extra_context)
    
    return render(request, template, context)








def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'powwows/post_detail.html', {'post': post})




