from django.shortcuts import render
from .forms import EventForm
from .models import Event
from django.views.generic import ListView

# Create your views here.
def index(request):
    return render(request,'dsc_app/index.html')
def about(request):
    return render(request,'dsc_app/about.html')


class EventListView(ListView):
    queryset = Event.objects.all()
    context_object_name = 'events'
    template_name = 'dsc_app/events.html'

        
            


    


