from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView

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


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = Post
    template_name_suffix = ''

    def get(self, request, *args, **kwargs):
        return self.post(request, *args, **kwargs)

    def get_success_url(self):
        return reverse_lazy('index')


# def json_like(request, id, *args, **kwargs):
#     like = get_object_or_404(Like, post_id=id)
#     if like:
#         like.delete()
#         return JsonResponse({'success': True, 'message': 'true', 'id': id})
#     like.get_or_crete(Like(post_id=id))
#     return JsonResponse({'success': True, 'message': 'false', 'id': id})
