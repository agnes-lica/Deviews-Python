from django.urls import path
from . import views

urlpatterns = [
    path("comments/post/<int:pk>/", views.CommentsView.as_view()),
    path("comments/<int:pk>/", views.CommentsDetailView.as_view())
]
