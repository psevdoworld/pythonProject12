from django.shortcuts import render
from blog.models import Post

def post_list(request):
    posts = Post.objects.all()
    return render(
        request,
        'post_list.html',
        {'postiki':posts},
    )

def post_details(request,post_id):
    post = Post.objects.filter(id=post_id).first()
    return render(
        request,
        'post_detail.html',
        {'post': post},
    )



