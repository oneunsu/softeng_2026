from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/board/tag/{self.slug}/'


class Post(models.Model):
    title = models.CharField(max_length=100)
    hook_text = models.CharField(max_length=200, blank=True)
    content = models.TextField()

    head_image = models.ImageField(
        upload_to='board/images/%Y/%m/%d/',
        blank=True
    )

    file_upload = models.FileField(
        upload_to='board/files/%Y/%m/%d/',
        blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.SET_NULL
    )

    category = models.ForeignKey(
        Category,
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )

    tags = models.ManyToManyField(
        Tag,
        blank=True
    )

    def __str__(self):
        if self.author:
            return f'[{self.pk}] {self.title} :: {self.author}'
        return f'[{self.pk}] {self.title} :: 작성자 없음'

    def get_absolute_url(self):
        return f'/board/{self.pk}/'