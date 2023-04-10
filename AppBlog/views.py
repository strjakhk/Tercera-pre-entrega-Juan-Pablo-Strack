from django.shortcuts import render
from .models import *
from .forms import *

# Create your views here.

def busqueda(request):
    users = Users.objects.all()
    title = request.GET["post-filter"]
    posts = Posts.objects.filter(post_title__icontains=title)
    return render(request, 'inicio.html', {'users' : users, 'posts' : posts})

def main(request):
    users = Users.objects.all()
    posts = Posts.objects.all()
    return render(request, 'inicio.html', {'users' : users, 'posts' : posts})

def registro(request):
    if request.method == "POST":
        form = Registro(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            user = Users(user_name = form_info['user_name'], user_pass = form_info['user_pass'], user_email = form_info['user_email'])
            user.save()
            return render(request, 'registro-valido.html')
        else:
            new_form = Registro()
            return render(request, 'registro-novalido.html', {'form' : new_form})
    else:
        new_form = Registro()
        return render(request, 'registro.html', {'form' : new_form})

def posts(request):
    if request.method == 'POST':
        form = Post(request.POST)
        if form.is_valid():
            form_info = form.cleaned_data
            post = Posts(post_author = form_info['post_author'], post_title = form_info['post_title'], post_content = form_info['post_content'])
            post.save()
            return render(request, 'articulo-publicado.html')
        else:
            form = Post()
            return render(request, 'articulo-novalido.html', { 'form' : form })
        
    else:
        form = Post()
        return render(request, 'posts.html', { 'form' : form })

def comentarios(request):
    if request.method == 'POST':
        comment_form = Comentarios(request.POST)
        if comment_form.is_valid():
            data = comment_form.cleaned_data
            new_comment = Comments(comment_author = data['comment_author'], comment_content = data['comment_content'])
            new_comment.save()
            return render(request, 'comentario_publicado.html')

        else:
            comment_form = Comentarios()
            return render(request, 'comentarios.html', { 'form' : comment_form})
    else:
        comment_form = Comentarios()
        return render(request, 'comentarios.html', { 'form' : comment_form})
