# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from stories.models import Author, ShortStory, Poem


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class ShortStoryListView(ListView):
    model = ShortStory


class ShortStoryDetailView(DetailView):
    model = ShortStory


class PoemListView(ListView):
    model = Poem


class PoemDetailView(DetailView):
    model = Poem
