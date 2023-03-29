from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import TemplateView

from accounts.models import Account


class AddFollowView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        following = get_object_or_404(Account, pk=kwargs['pk'])
        obj = Account.object.get(pk=user.pk)
        obj.add_following(following)
        return redirect('account', pk=kwargs['pk'])


class DeleteFollowView(LoginRequiredMixin, TemplateView):
    def post(self, request, *args, **kwargs):
        user = request.user
        follow = get_object_or_404(Account, pk=kwargs['pk'])
        obj = Account.object.get(pk=user.pk)
        obj.following.remove(follow)
        return redirect('account', pk=kwargs['pk'])
