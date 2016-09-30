from django.shortcuts import render
from .models import Post

# Create your views here.
def load_map(request):
    posts = Post.all_posts.all()
    return render(request,'main/map.html',{'posts':posts})
