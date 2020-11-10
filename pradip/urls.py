from . import views
from django.urls import path
from django.conf.urls import url

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog_list'),
    # path('thanks/', views.thanks, name='thanks'),
    path('blog/<slug:slug>', views.blog_detail, name='blog_detail'),

    path('album/', views.album, name='album_list'),

    # path('album/<slug:slug>', views.album_detail, name='album_detail')

]
