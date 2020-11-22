from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, DeleteView 
from . models import Post

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'


class DetailPageView(DetailView):
    model = Post
    template_name = 'detail.html'


@method_decorator(login_required, name="dispatch")
class NewPost(CreateView):
    model = Post
    template_name = 'novo.html'
    fields = '__all__'
    success_url = '/'


@method_decorator(login_required, name="dispatch")
class Deletar(DeleteView):
    model = Post
    template_name = 'deletar.html'
    success_url = '/'
