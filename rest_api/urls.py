from django.urls import path, include
# from .views import PostsView, posts_detail
from .views import PostsAPIViews, posts_detailsAPIViews
# from .views import genericApiView
# from .views import PostViewSets
from rest_framework import routers

# ----- using viewSets & Routers ------
# router = routers.SimpleRouter()

# router.register('posts', PostViewSets, basename='posts')

urlpatterns = [

    # urls using function based views
    # path('posts/', PostsView),
    # path('details/<int:pk>', posts_detail)
    
    # urls using class-based views
    path('postsAPIViews/', PostsAPIViews.as_view()),
    path('detailsAPIViews/<int:pk>', posts_detailsAPIViews.as_view())

    # using mixins and generic class-based views
    # path('genericApiView/', genericApiView.as_view()),
    # path('genericApiView/<int:id>/', genericApiView.as_view()),

    #using viewSets & Routers
    # path('',include(router.urls)),
]