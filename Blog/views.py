from django.shortcuts import render, get_object_or_404, redirect
from .models import BlogPost
from .forms import CommentForm, BlogPostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required


def blog_list(request):
    posts = BlogPost.objects.filter(parent__isnull=True).order_by('-created_at')
    return render(request, 'blog/blog_list.html', {'posts': posts})

def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, id=post_id)
    post.views += 1
    post.save()
    comments = post.comments.all()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.user = request.user
            comment.save()
            return redirect('blog_detail', post_id=post.id)
    else:
        form = CommentForm()

    return render(request, 'blog/blog_detail.html', {
        'post': post,
        'comments': comments,
        'form': form,
    })

def blog_search(request):
    query = request.GET.get('q')
    results = BlogPost.objects.filter(title__icontains=query) if query else BlogPost.objects.none()
    return render(request, 'blog/blog_search.html', {'query': query, 'results': results})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_blog_post(request):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            blog_post = form.save(commit=False)
            blog_post.author = request.user  # Set the logged-in user as the author
            blog_post.save()
            return redirect('blog_list')  # Redirect to the blog list after creation
    else:
        form = BlogPostForm()
    return render(request, 'blog/create_blog_post.html', {'form': form})

@login_required
def edit_blog_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=blog_post)
        if form.is_valid():
            form.save()
            return redirect('blog_detail', post_id=post_id)  # Redirect to the post details page
    else:
        form = BlogPostForm(instance=blog_post)
    return render(request, 'blog/edit_blog_post.html', {'form': form})

@login_required
def delete_blog_post(request, post_id):
    blog_post = get_object_or_404(BlogPost, id=post_id, author=request.user)
    if request.method == 'POST':
        blog_post.delete()
        return redirect('blog_list')  # Redirect to the blog list after deletion
    return render(request, 'blog/delete_blog_post.html', {'blog_post': blog_post})
