from django.urls import path

from blogs.apps import BlogsConfig
from blogs.views import BlogListview, BlogDetailview, BlogCreateView, BlogUpdateView, BlogDeleteView

app_name = BlogsConfig.name

urlpatterns = [
    path('blog/', BlogListview.as_view(), name='blog_list'),
    path('blog/<int:pk>/', BlogDetailview.as_view(), name='blog_detail'),
    path('blog/create/', BlogCreateView.as_view(), name='blog_create'),
    path('blog/<int:pk>/update/', BlogUpdateView.as_view(), name='blog_update'),
    path('blog/<int:pk>/delete/', BlogDeleteView.as_view(), name='blog_delete'),

]