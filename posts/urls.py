from django.urls import path

from posts.views.base import IndexView, IndexRedirectView
from posts.views.comments import CommentCreateView
from posts.views.likes import LikeView, DislikeView
from posts.views.posts import PostCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/", IndexRedirectView.as_view(), name="post_index_redirect"),
    path("post/create", PostCreateView.as_view(), name="post_create"),
    path(
        "post/<int:pk>/comment/create",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path("post/<int:pk>/like", LikeView.as_view(), name="like"),
    path("post/<int:pk>/dislike", DislikeView.as_view(), name="dislike"),
]
