from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Snack
# from django.db import models


class SnackListView(ListView):
    model = Snack
    template_name = 'snack_list.html'
    context_object_name = 'order_object'

    # def get_queryset(self):
    #     return models.Snack.objects.all()

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
