from django.shortcuts import render,get_object_or_404
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

def event_detail(request, year, month, day, event):
    event = get_object_or_404(Event,slug=event,
                                    status='published',
                                    publish__year=year,
                                    publish__month=month,
                                    publish__day=day)
    return render(request,'dsc_app/detail.html',{'event': event})

def create_event(request):
    if request.method == 'POST':
        #submitted event
        form = EventForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            form.save()
    else:
        form = EventForm()
    return render(request,'dsc_app/create.html',{'form':form})





        
            


    


