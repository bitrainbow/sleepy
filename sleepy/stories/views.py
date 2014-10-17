# from django.shortcuts import render
from django.views.generic import DetailView, ListView
from models import Author, ShortStory, Poem


class AuthorListView(ListView):
    model = Author


class AuthorDetailView(DetailView):
    model = Author


class ShortStoryListView(ListView):
    model = ShortStory
    template_name = 'base_shortstoryindex.html'


class ShortStoryDetailView(DetailView):
    model = ShortStory
    template_name = 'base_shortstorydetail.html'


class PoemListView(ListView):
    model = Poem
    template_name = 'base_poemindex.html'


class PoemDetailView(DetailView):
    model = Poem
    template_name = 'base_poemdetail.html'
