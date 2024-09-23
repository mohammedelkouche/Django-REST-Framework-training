from django.urls import path
# from .views import PostsView, posts_detail
from .views import PostsAPIViews, posts_detailsAPIViews

urlpatterns = [

    # urls using function based views
    # path('posts/', PostsView),
    # path('details/<int:pk>', posts_detail)
    
    # urls using class-based views
    path('postsAPIViews/', PostsAPIViews.as_view()),
    path('detailsAPIViews/<int:pk>', posts_detailsAPIViews.as_view())


]