from django.shortcuts import render,get_object_or_404
from .forms import EventForm
from .models import Event
from django.views.generic import ListView

# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request,'dsc_app/index.html',{'events':events})
    
def about(request):
    return render(request,'dsc_app/about.html')

def event_detail(request, year, month, day, event):
    event = get_object_or_404(Event,slug=event,
                                    # status='published',
                                    published__year=year,
                                    published__month=month,
                                    published__day=day)
    return render(request,'dsc_app/detail.html',{'event': event})

def create_event(request):
    #list of published events
    # events = Event.objects.filter(published=True)

    new_event = None

    if request.method == 'POST':
        #an event was published
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            #create event object and save
            new_event = event_form.save()
    else:
        event_form = EventForm()
    
    return render(request,'dsc_app/create.html',{'new_event':new_event,'event_form':event_form})
            




        
            


    


