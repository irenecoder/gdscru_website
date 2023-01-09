from django.shortcuts import render,get_object_or_404,redirect
from .forms import EventForm
from .models import Event
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views.generic import ListView

# Create your views here.
def index(request):
    events = Event.objects.all()
    return render(request,'dsc_app/index.html',{'events':events})
    
def about(request):
    return render(request,'dsc_app/about.html')

def event_list(request):
    events = Event.objects.all()
    return render(request,'dsc_app/events.html',{'events':events})

def event_detail(request, year, month, day, event,id):
    event = get_object_or_404(Event,slug=event,
                                    # status='published',
                                    published__year=year,
                                    published__month=month,
                                    published__day=day)
    
    return render(request,'dsc_app/detail.html',{'event': event})

def create_event(request):
    """Add a new event"""
    if request.method != 'POST':
        #No data submitted;create a blank form
        form = EventForm()
    else:
        #POST data submitted;process data
        form = EventForm(request.POST) 
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('dsc_app:event_list'))
    context = {'form':form}
    return render(request,'dsc_app/create.html',context)

def delete_event(request,id):
    deleted_event = get_object_or_404(Event,id=id)
    deleted_event.delete()
    redirect('dsc_app/index.html')



            




        
            


    


