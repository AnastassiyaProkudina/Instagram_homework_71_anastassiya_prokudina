from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import RedirectView, CreateView

from posts.forms import PostForm
from posts.models import Post


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm

    def get_success_url(self):
        return self.request.META.get("HTTP_REFERER")

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class IndexRedirectView(RedirectView):
    pattern_name = "posts:index"
