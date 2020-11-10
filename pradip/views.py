# from django.views import generic
# class BlogList(generic.ListView):
#     queryset = Blog.objects.filter(status=1).order_by('-created_on')
#     template_name = 'index.html'

# class BlogDetail(generic.DetailView):
#     model = Blog
#     template_name = 'blog_detail.html'


from django.http import HttpResponse
from django.shortcuts import render
from .models import Blog
from .models import Album
from .models import Gallery
from django.core.mail import send_mail
from django.conf import settings
# from .forms import ContactForm


def index(request):
    blogs = Blog.objects.all()

    if request.method == 'POST':
        c_name = request.POST['c_name']
        # c_subject = request.POST['c_subject']
        c_message = request.POST['c_message']
        c_email = request.POST['c_email']

        send_mail(
            c_email,
            c_message,
            c_email,  # from
            ['pradip.subedi@live.com', 'kindhearted98@gmail.com']
        )

        return render(request, 'all/thanks.html', {'c_name': c_name})
    else:
        return render(request, 'all/index.html', {'blogs': blogs})


# def thanks(request):
#     c_name = request.POST['c_name']
#     return render(request, 'all/thanks.html', {'c_name': c_name})


def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'all/blog.html', {'blogs': blogs})


def blog_detail(request, slug):
    blogs = Blog.objects.all()
    blog = Blog.objects.get(slug=slug)
    return render(request, 'all/blog_detail.html', {'blog': blog, 'blogs': blogs})


def album(request):
    albums = Album.objects.all()
    return render(request, 'all/album.html', {'albums': albums})


# def album_detail(request, slug):
#     albums = Album.objects.all()
#     album = Album.object.get(slug=slug)
#     return render(request, 'all/album_detail.html', {'albums': albums, 'album': album})
