from django.urls import path

from accounts.views import *
from posts.views.follows import AddFollowView, DeleteFollowView
from posts.views.likes import LikeView

urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", logout_view, name="logout"),
    path("register/", RegisterView.as_view(), name="register"),
    path("account/<int:pk>", AccountView.as_view(), name="account"),
    path("account/<int:pk>/change", UserChangeView.as_view(), name="change"),
    path("account/<int:pk>/add_follow", AddFollowView.as_view(), name="follow"),
    path("account/<int:pk>/delete_follow", DeleteFollowView.as_view(), name="unfollow"),
]
