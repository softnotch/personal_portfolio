from django.shortcuts import render, get_object_or_404
from .models import AllBlog

# Create your views here.
def all_blogs(request):
    blogs = AllBlog.objects.order_by('-date') [:3]
    return render(request,'blog/all_blogs.html' ,{'blogs':blogs})

def about (request):
    return render(request, 'blog/about.html')

def detail(request, blog_id):
    blog = get_object_or_404(AllBlog, pk=blog_id)
    return render (request, 'blog/detail.html', {'blog': blog},)