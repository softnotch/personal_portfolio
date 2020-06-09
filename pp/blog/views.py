from django.shortcuts import render
from .models import AllBlog

# Create your views here.
def all_blogs(request):
    blogs = AllBlog.objects.order_by('-date') [:3]
    return render(request,'blog/all_blogs.html' ,{'blogs':blogs})

def about (request):
    return render(request, 'blog/about.html')