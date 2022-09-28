from django.urls import path
from  . import views

app_name = 'dsc_app'
urlpatterns = [
    path('',views.index,name="index"),
    path('about/', views.about,name="about"),
    path('event/',views.EventListView.as_view(),name="events"),
]