from django.urls import path
from . import views

urlpatterns = [
    path("posts/", views.PostView.as_view()),
    path("posts/<int:pk>/", views.PostDetailView.as_view()),
    path("posts/user/<int:pk>/", views.PostUserDetailViews.as_view()),
]
