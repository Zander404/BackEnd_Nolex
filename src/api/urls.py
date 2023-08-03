from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views


urlpatterns = [
    path("user/", views.UserList.as_view()),
    path("user/<int:pk>", views.UserDetail.as_view()),
    path("projects/", views.ProjectList.as_view()),
    path("projects/<int:pk>", views.ProjectDetail.as_view()),
    path('skill/', views.SkillList.as_view()),
    path('skill/<int:pk>', views.SkillDetail.as_view()),
    

]

urlpatterns = format_suffix_patterns(urlpatterns)
