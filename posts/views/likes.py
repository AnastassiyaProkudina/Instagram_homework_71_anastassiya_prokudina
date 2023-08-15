from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from accounts.models import Account
from posts.models import Post, Like


class LikeView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        liked_post = get_object_or_404(Post, pk=request.POST.get('pk'))
        author = get_object_or_404(Account, pk=request.user.pk)
        try:
            like = Like.objects.get(author=author, post=liked_post)
            like.delete()
            post_likes_count = liked_post.likes.count()
            return JsonResponse({'success': True, 'like_added': False, 'post_likes_count': post_likes_count})
        except Like.DoesNotExist:
            Like.objects.create(author=author, post=liked_post)
            post_likes_count = liked_post.likes.count()
            return JsonResponse({'success': True, 'like_added': True, 'post_likes_count': post_likes_count})

