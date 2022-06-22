from django.shortcuts import render
from django.views.generic.edit import  CreateView, UpdateView, DeleteView
from django.views.generic.list import  ListView
from django.views.generic.detail import DetailView

from .models import Todoapp

# Create your views here.

class TodoappCreateView(CreateView):
    model = Todoapp
    fields = [
        'title',
        'description'
    ]
    template_name = 'home.html'
    success_url = 'list.html'

class TodoappListView(ListView):
    model = Todoapp
    template_name = 'list.html'

class TodoappDetailView(DetailView):
    model = Todoapp
    template_name = 'detail.html'

class TodoappUpdateView(UpdateView):
    model = Todoapp

    fields = [
        "title",
        "description",
    ]
    template_name = 'update.html'
    success_url= '/'

class TodoappDeleteView(DeleteView):
    model = Todoapp
    template_name = 'delete.html'
    success_url= '/'