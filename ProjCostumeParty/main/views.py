from django.shortcuts import render, redirect
from .models import Post
from .forms import PostForm
from django.http import HttpResponseRedirect

# Create your views here.
def load_map(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    elif request.method == 'GET':
        posts = Post.all_posts.all()
        form = PostForm()
    return render(request,'main/map.html',{'posts':posts,'form':form})

# def post_new(request):
#     if request.method == "POST":
#         form = PostForm(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponseRedirect('/')
#     else:
#         form = PostForm()
#         # return HttpResponse('Allowed only via POST')
#     return render(request, 'main/map.html', {'form': form})
