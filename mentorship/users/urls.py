from django.urls import path
from . import views

urlpatterns = [  
    path('users/', views.UserList.as_view()), 
    path('users/<int:pk>/', views.UserDetail.as_view()),
    path('users/self/', views.CurrentUserView.as_view()),
    path('users/skills/', views.SkillView.as_view()),
]