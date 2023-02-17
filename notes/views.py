from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from .models import Notes
from django.views.generic import ListView,CreateView , DetailView

class models(ListView):
    model = Notes
    context_object_name = "notes"
    template_name = 'notes/notes_list.html'

class NotesCreateView(CreateView):
    model = Notes
    fields = ['title','text']
    success_url =  'smart/notes'

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.html',{'notes':all_notes})
# Create your views here.

class detail(DetailView):
    model = Notes
    context_object_name = "note"
    template_name = 'notes/notes_detail.html'

# def details(request,pk):
#     try:
#         note = Notes.objects.get(pk = pk)
#     except Notes.DoesNotExist:
#         raise Http404("Node doesn't exist")
#     return render(request, 'notes/notes_detail.html',{'note':note})

        
