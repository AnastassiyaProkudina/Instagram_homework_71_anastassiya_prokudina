from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse
from django.views.generic import (
    TemplateView,
    CreateView,
    DetailView,
    UpdateView,
)

from accounts.forms import LoginForm, CustomUserCreationForm, AddFollowForm
from accounts.models import Account
from posts.forms import PostForm


class LoginView(TemplateView):
    template_name = "login.html"
    form = LoginForm

    def get(self, request, *args, **kwargs):
        form = self.form()
        context = {"form": form}
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = self.form(request.POST)
        if not form.is_valid():
            messages.error(request, "Некорректные данные")
            return redirect("index")
        email = form.cleaned_data.get("email")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if not user:
            messages.warning(request, "Пользователь не найден")
            return redirect("index")
        login(request, user)
        next = request.GET.get("next")
        if next:
            return redirect(next)
        return redirect("index")


def logout_view(request):
    logout(request)
    return redirect("index")


class RegisterView(CreateView):
    template_name = "register.html"
    form_class = CustomUserCreationForm
    success_url = "/"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect(self.success_url)
        context = {"form": form}
        return self.render_to_response(context)


class AccountView(LoginRequiredMixin, DetailView):
    model = get_user_model()
    template_name = "user_detail.html"
    context_object_name = "user_obj"

    def get_context_data(self, **kwargs):
        posts = self.object.posts.order_by("-created_at")
        kwargs["posts_count"] = posts.count()
        kwargs["followers_count"] = self.object.user_following.count()
        kwargs["following_count"] = self.object.following.count()
        kwargs["post_form"] = PostForm()

        return super().get_context_data(**kwargs)


class UserChangeView(UpdateView):
    model = get_user_model()
    form_class = UserChangeForm
    template_name = "user_change.html"
    context_object_name = "user_obj"

    def get_success_url(self):
        return reverse("account", kwargs={"pk": self.object.pk})


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
        obj.delete_following(follow)
        return redirect('account', pk=kwargs['pk'])
