from django.shortcuts import render
from .models import Post, Categoria
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.core.paginator import Paginator


# Create your views here.

def home(request):
    queryset= request.GET.get("buscar")
    posts = Post.objects.filter(estado = True)
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) | 
            Q(description__icontains = queryset) 
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'index.html', {'posts':posts})
#print(request.GET) -- Confirmar si el boton envia la informacion introducida


def detallePost(request,slug):
    post= get_object_or_404(Post, slug =slug)
    return render(request, 'post.html', {'detalle_post':post})


def generales1(request):
    queryset= request.GET.get("buscar")
    posts = Post.objects.filter(
        estado= True, 
        Categoria= Categoria.objects.get(nombre__iexact = 'General')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(description__icontains = queryset),
            estado= True,
            Categoria= Categoria.objects.get(nombre__iexact= "General"),
              
        ).distinct()
    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    return render(request, 'generales1.html',{'posts':posts})

def programacion(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado= True,
        Categoria= Categoria.objects.get(nombre__iexact= 'Programación')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(description__icontains = queryset),
            estado = True,
            Categoria = Categoria.objects.get(nombre__iexact = "Programación")
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    return render(request, 'programacion.html', { 'posts': posts})

def videojuegos(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado= True,
        Categoria= Categoria.objects.get(nombre__iexact= 'Videojuegos')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(description__icontains = queryset),
            estado = True,
            Categoria = Categoria.objects.get(nombre__iexact = "Videojuegos")
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'videojuegos.html', {'posts': posts})

def tecnologia(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado= True,
        Categoria= Categoria.objects.get(nombre__iexact= 'Tecnología')
    )
    if queryset:
        posts= Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(description__icontains = queryset),
            estado = True,
            Categoria= Categoria.objects.get(nombre__iexact= 'Tecnología')

        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)

    
    return render(request,'tecnologia.html', {'posts':posts})

def tutoriales(request):
    queryset = request.GET.get("buscar")
    posts = Post.objects.filter(
        estado= True,
        Categoria= Categoria.objects.get(nombre__iexact= 'Tutoriales')
    )
    if queryset:
        posts = Post.objects.filter(
            Q(titulo__icontains = queryset) |
            Q(description__icontains = queryset),
            estado = True,
            Categoria = Categoria.objects.get(nombre__iexact = "Tutoriales")
        ).distinct()

    paginator = Paginator(posts, 2)
    page = request.GET.get('page')
    posts = paginator.get_page(page)


    return render(request, 'tutoriales.html', {'posts':posts})