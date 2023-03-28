from django.urls import path

from posts.views.base import IndexView, IndexRedirectView
from posts.views.comments import CommentCreateView
from posts.views.posts import PostCreateView

urlpatterns = [
    path("", IndexView.as_view(), name="index"),
    path("article/", IndexRedirectView.as_view(), name="post_index_redirect"),
    path("post/create", PostCreateView.as_view(), name="post_create"),
    path(
        "post/<int:pk>/comment/create",
        CommentCreateView.as_view(),
        name="comment_create",
    ),
]
