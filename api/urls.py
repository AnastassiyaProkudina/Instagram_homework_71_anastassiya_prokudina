from django.urls import path, include
from rest_framework import routers

# from api.views.comments import CommentView
# from api.views.likes import LikeView
# from api.views.posts import PostView
#
# router = routers.DefaultRouter()
# router.register('posts', PostView)
# router.register('likes', LikeView)
# router.register('comments', CommentView)

urlpatterns = [
    path("", include(router.urls)),
]
