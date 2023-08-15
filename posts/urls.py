from django.urls import path

from posts.views.base import IndexView, IndexRedirectView
from posts.views.comments import CommentCreateView
from posts.views.likes import LikeView
from posts.views.posts import PostCreateView, PostDeleteView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("post/", IndexRedirectView.as_view(), name="post_index_redirect"),
    path("post/create", PostCreateView.as_view(), name="post_create"),
    path("post/<int:pk>/delete", PostDeleteView.as_view(), name="post_delete"),
    path(
        "post/<int:pk>/comment/create",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
    path("post/like", LikeView.as_view(), name="like"),
]
