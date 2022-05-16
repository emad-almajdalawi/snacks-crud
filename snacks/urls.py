from django.urls import path
from .views import SnackListView, SnackDetailView, SnackCreateView, SnackUpdateView, SnackDeleteView

urlpatterns = [
    path('', SnackListView.as_view(), name='snack_list'),
    path('snacks-details/<int:pk>', SnackDetailView.as_view(), name='snack_detail'),
    path('create-snack/', SnackCreateView.as_view(), name='snack_new'),
    path('update-snack/<int:pk>', SnackUpdateView.as_view(), name='snack_edit'),
    path('delete-snack/<int:pk>', SnackDeleteView.as_view(), name='snack_delete'),
]