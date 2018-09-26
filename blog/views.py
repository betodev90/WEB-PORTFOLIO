from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import Post
# Create your views here.

def lista_posts(request):
    posts = Post.objects.filter(publicado=True).order_by('titulo')
    print('lista de posts: ', posts)
    return render(request, 'blog/lista_posts.html', {'posts': posts}
    )

def posts_detalle(request, id):
    detalle_post = get_object_or_404(Post, pk=id)
    return render(request, 'blog/detalle_post.html', 
        {
            'post': detalle_post
        }
    )