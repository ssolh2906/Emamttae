import datetime

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User



# Create your models here.
from django.urls import reverse


class Board(models.Model):
    title = models.CharField("TITLE", max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True)
    description = models.CharField('DESCRIPTION', max_length=100, blank=True)
    created_date = models.DateField('CREATED DATE', auto_now_add=True)
    modified_date = models.DateField('MODIFIED DATE', auto_now=True)

    class Meta:
        verbose_name = 'board'
        verbose_name_plural = 'boards'
        ordering = ('-modified_date',)

    def __str__(self):
        return self.slug

    def get_absolute_url(self):
        return reverse('board:board_detail', args=(self.slug,))


class Post(models.Model):
    board = models.ForeignKey(Board,on_delete=models.CASCADE, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField('POST', max_length=100)
    slug = models.SlugField('SLUG', unique=True, allow_unicode=True)
    content = models.TextField('CONTENT')
    created_date = models.DateTimeField('CREATED DATE', default=timezone.now)
    modified_date = models.DateTimeField('MODIFIED DATE', default=timezone.now)
    created_week = models.IntegerField('CREATED_WEEK', default=timezone.now().isocalendar()[1],)

    class Meta:
        verbose_name = 'post'
        verbose_name_plural = 'posts'
        ordering = ('-created_date',)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('board:post_detail', args=self.slug, )

    def get_previous(self):
        return self.get_previous_in_order()

    def get_next(self):
        return self.get_next_in_order()
