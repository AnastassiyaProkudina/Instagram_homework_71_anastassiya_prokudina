from django.db.models import Q
from django.utils.http import urlencode
from django.views.generic import RedirectView, TemplateView

from accounts.models import Account
from posts.forms import CommentForm, PostForm
from accounts.forms import SearchForm, LoginForm
from posts.models import Post, Like


class IndexView(TemplateView):
    template_name = "index.html"
    form_class = LoginForm

    def get(self, request, *args, **kwargs):
        self.form = self.get_search_form()
        self.search_value = self.get_search_value()
        return super().get(request, *args, **kwargs)

    def get_search_form(self):
        return SearchForm(self.request.GET)

    def get_search_value(self):
        if self.form.is_valid():
            return self.form.cleaned_data["search"]
        return None

    def get_queryset(self):
        queryset = Account.objects.all()
        if self.search_value:
            query = (
                Q(username__icontains=self.search_value)
                | Q(email__icontains=self.search_value)
                | Q(first_name__icontains=self.search_value)
            )
            queryset = queryset.filter(query)
        return queryset

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        context["search_form"] = SearchForm()
        context["form"] = self.form_class
        context["comment_form"] = CommentForm()
        context["post_form"] = PostForm()
        context["posts"] = Post.objects.all().order_by("-created_at")
        context["accounts"] = Account.objects.all()
        user = self.request.user
        if user.is_authenticated:
            context["user_likes"] = Like.objects.filter(author=user).values_list("post_id", flat=True)
        else:
            context["user_likes"] = []

        if self.search_value:
            context["query"] = urlencode({"search": self.search_value})
            context["search_accounts"] = self.get_queryset()
        return context


class IndexRedirectView(RedirectView):
    pattern_name = "index"
