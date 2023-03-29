from django.contrib.auth import get_user_model
from django.db import models


class Post(models.Model):
    text = models.TextField(
        verbose_name="Текст", null=False, max_length=2200, blank=True
    )
    image = models.ImageField(
        verbose_name="Фото", null=False, blank=False, upload_to="posts"
    )
    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="posts",
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )


class Comment(models.Model):
    author = models.ForeignKey(
        verbose_name="Автор",
        to=get_user_model(),
        related_name="comments",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        verbose_name="Публикация",
        to="posts.Post",
        related_name="comments",
        on_delete=models.CASCADE,
    )
    text = models.TextField(
        verbose_name="Комментарий", null=False, blank=False, max_length=200
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Время создания",
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата и время обновления",
    )

    def __str__(self):
        return self.text[:20]


# class Like(models.Model):
#     author = models.ForeignKey(
#         verbose_name="Автор",
#         to=get_user_model(),
#         related_name="likes",
#         on_delete=models.CASCADE,
#     )
#     post = models.ForeignKey(
#         verbose_name="Публикация",
#         to="posts.Post",
#         related_name="likes",
#         on_delete=models.CASCADE,
#     )
