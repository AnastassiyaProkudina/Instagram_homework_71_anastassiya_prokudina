from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import TextChoices

from accounts.managers import UserManager


class GenderChoice(TextChoices):
    MALE = "MALE", "Мужчина"
    FEMALE = "FEMALE", "Женщина"


class Account(AbstractUser):
    email = models.EmailField(
        verbose_name="Электронная почта", unique=True, blank=False
    )

    avatar = models.ImageField(
        null=True, blank=False, upload_to="user_pic", verbose_name="Аватар"
    )
    bio = models.TextField(verbose_name="Информация о пользователе", blank=True)
    phone = models.CharField(verbose_name="Номер телефона", blank=True, max_length=30)
    gender = models.CharField(
        verbose_name="Пол", choices=GenderChoice.choices, blank=True, max_length=40
    )

    liked_posts = models.ManyToManyField(
        verbose_name="Понравившиеся публикации",
        to="posts.Post",
        related_name="user_likes",
        blank=True,
    )
    following = models.ManyToManyField(
        verbose_name="Подписки",
        to="accounts.Account",
        related_name="user_following",
        blank=True,
    )
    commented_posts = models.ManyToManyField(
        verbose_name="Прокомментированные публикации",
        to="posts.Post",
        related_name="user_comments",
        blank=True,
    )
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    object = UserManager()

    class Meta:
        verbose_name = "Профиль"
        verbose_name_plural = "Профили"

    def __str__(self):
        return self.username
