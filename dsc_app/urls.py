from django.urls import path
from  . import views

app_name = 'dsc_app'
urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.about,name="about"),
    path('<int:year>/<int:month>/<int:day>/<slug:event>/',views.event_detail,name="event_detail"),
    path('create/', views.create_event,name="create"),
]