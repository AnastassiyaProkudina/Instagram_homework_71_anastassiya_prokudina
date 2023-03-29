from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from accounts.models import Account
from posts.models import Post


class LikeView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        liked_post = get_object_or_404(Post, pk=kwargs['pk'])
        obj = Account.object.get(pk=request.user.pk)
        obj.liked_posts.add(liked_post)
        return redirect(self.request.META.get("HTTP_REFERER"))


class DislikeView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        liked_post = get_object_or_404(Post, pk=kwargs['pk'])
        obj = Account.object.get(pk=request.user.pk)
        obj.liked_posts.remove(liked_post)
        return redirect(self.request.META.get("HTTP_REFERER"))
