from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

# Create your views here.
def index(request):
    return render(request, 'blog/index.html', {})

def udesk(request):
    return render(request, 'blog/u-desk.html', {})

def curtain(request):
    return render(request, 'blog/curtain.html', {})

def armband(request):
    return render(request, 'blog/armband.html', {})

def nosotros(request):
    return render(request, 'blog/nosotros.html', {})

def comunidad(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/comunidad.html', {'posts': posts})