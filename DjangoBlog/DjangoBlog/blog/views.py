from django.shortcuts import render,get_object_or_404,redirect
from django.http import HttpResponse
from .models import BlogPost
from django.utils import timezone
from .forms import PostForm

# Create your views here.
def post_list(request):
    # post=BlogPost.objects.order_by('-created_date')
    post =BlogPost.objects.filter(published_date__lte=timezone.now())
    # return render(request,'blog_pages/post_list.html',{'posts':post})
    return render(request, 'blog_pages/post_list.html', {'data': post})
    # return HttpResponse(post)
#
def about(request):
    return render(request,'blog_pages/post_list.html')
    return HttpResponse("this is about us page")

def post_detail(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)
    return render(request,'blog_pages/post_detail.html',{'post':post})

def post_remove(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)
    post.delete()
    return redirect('post_list')

def post_edit(request,pk):
    post=get_object_or_404(BlogPost,pk=pk)
    if request.method=="POST":
        form=PostForm(request.POST,instance=post)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.published_date=timezone.now()
            post.save()
            return  redirect('post_detail',pk=post.pk)
    else:
        form =PostForm(instance=post)
    return render(request,'blog_pages/post_edit.html',{'form':form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.created_date = timezone.now()
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)

    else:
        form=PostForm()
    return render(request,'blog_pages/post_edit.html', {'form': form})