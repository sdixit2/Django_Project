from django.urls import path

from . import views

urlpatterns = [
    path('notes', views.models.as_view(), name = "notes.list"),
    path('notes/<int:pk>', views.detail.as_view(), name = "notes.detail"),
    path('notes/new', views.NotesCreateView.as_view(), name = "notes.new"),
 ]