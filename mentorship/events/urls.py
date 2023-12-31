from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [ 
  path('events/', views.EventList.as_view()),
  path('events/<int:pk>/', views.EventDetail.as_view()),
  path('mentor-events/', views.EventMentorList.as_view()),
  path('mentor-events/<int:pk>/', views.EventMentorDetail.as_view()),
  path('mentor-events/self/', views.MyEvents.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)