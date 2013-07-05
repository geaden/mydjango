
from django.views.generic import \
    CreateView, DetailView, ListView, UpdateView, DeleteView

from .models import MyModel
from .forms import MyModelForm


class MyModelCreateView(CreateView):
    model = MyModel
    form_class = MyModelForm


class MyModelUpdateView(UpdateView):
    model = MyModel
    form_class = MyModelForm


class MyModelDetailView(DetailView):
    model = MyModel


class MyModelListView(ListView):
    model = MyModel


class MyModelDeleteView(DeleteView):
    model = MyModel

