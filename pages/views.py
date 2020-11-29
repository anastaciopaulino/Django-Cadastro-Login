from django.shortcuts import render
from django.views.generic import ListView, DetailView 
from django.views.generic.edit import CreateView, DeleteView, UpdateView 
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
    fields = ('title', 'summary', 'content')
    success_url = '/'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.author = self.request.user

        self.object.save()

        return super().form_valid(form)


@method_decorator(login_required, name="dispatch")
class Deletar(DeleteView):
    model = Post
    template_name = 'deletar.html'
    success_url = '/'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(author_id=self.request.user.id)


class UpdatePageView(UpdateView):
    model = Post
    template_name ='editar.html'
    fields = '__all__'
    success_url = '/'


