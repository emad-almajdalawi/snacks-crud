from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack


class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'
    context_object_name = 'order_object'


class SnackDetailView(DetailView):
    model = Snack
    template_name = 'snack_detail.html'


class SnackCreateView(CreateView):
    model = Snack
    template_name = 'snack_new.html'
    fields = ['title', 'purchaser', 'description']


class SnackUpdateView(UpdateView):
    model = Snack
    template_name = 'snack_edit.html'
    fields = ['title', 'description']


class SnackDeleteView(DeleteView):
    model = Snack
    template_name = 'snack_delete.html'
    success_url = '/'
