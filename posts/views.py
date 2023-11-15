from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm,CommentForm
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

# Create your views here.

def index(request):
    posts = Post.objects.all().order_by('-id')
    form = CommentForm()

    context = {
        'posts': posts,
        'form': form,
    }
    return render(request, 'index.html', context)

@login_required
def create(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user
            post.save()
            return redirect('posts:index')

    else:
        form = PostForm()
    context = {
        'form': form,
    }
    return render(request, 'form.html', context)


@login_required
def detail(request, id):
    post = Post.objects.get(id=id)
    form = CommentForm()

    context = {
        'post': post,
        'form': form,
    }
    return render(request, 'detail.html', context)



@login_required
def likes(request, id):
    user = request.user
    post = Post.objects.get(id=id)

    # 이미 좋아요 버튼을 누른경우
    # if post in user.like_posts.all():
    if user in post.like_users.all():
        post.like_users.remove(user)

    # 좋아요 버튼을 아직 누르지 않은 경우
    else:
        post.like_users.add(user)


    # user.like_posts.add(post)
    return redirect('posts:index')




@login_required
def comment_create(request, post_id):
    form = CommentForm(request.POST)

    if form.is_valid():
        comment = form.save(commit=False)

        comment.user_id = request.user.id
        comment.post_id = post_id

        comment.save()

        return redirect('posts:index')
    



@login_required
def comment_delete(request, post_id, id):
    comment = Comment.objects.get(id=id)

    if request.user == comment.user:
        comment.delete()

    return redirect('posts:index')
    



def likes_async(request, id):

    user = request.user
    post = Post.objects.get(id=id)

    if user in post.like_users.all():
        post.like_users.remove(user)
        status = False
    else:
        post.like_users.add(user) 
        status = True
    
    context = {
        'status': status,
        'count': len(post.like_users.all()),
    }

    return JsonResponse(context)


   


