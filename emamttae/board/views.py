import datetime

from django.shortcuts import render, get_object_or_404
from django.template import Context
from django.views.generic import ListView, DetailView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy

from .models import Board, Post


# ListView
class BoardLV(ListView):
    model = Board
    template_name = 'board/board_all.html'
    context_object_name = 'boards'
    paginate_by = 5


# DetailView
class Board_POSTLV(ListView):
    # model = Board
    week = datetime.datetime.now().isocalendar()[1]
    template_name = 'board/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.board_slug = self.kwargs['slug']
        return Post.objects.filter( created_week=self.week)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week'] = self.week

        return context


class Board_POSTLV_otherweeks(ListView):
    # model = Board
    template_name = 'board/post_list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.week = self.kwargs['week']
        return Post.objects.filter(created_week=self.week)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['week']=self.week
        return context




class PostCreatedView(LoginRequiredMixin, CreateView):
    model = Post
    fields = ['title', 'content']
    success_url = reverse_lazy('board:index')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)
