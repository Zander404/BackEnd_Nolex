from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>', views.PostDetail.as_view()),

    path('comment/', views.CommentList.as_view()),
    path('comment/<int:pk>', views.CommentDetail.as_view()),

    path('categorie/', views.CategorieList.as_view()),
    path('categorie/<int:pk>', views.CategorieDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)