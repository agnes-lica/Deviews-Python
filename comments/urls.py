from django.urls import path
from . import views

urlpatterns = [
    path("posts/<int:pk>/comments/", views.commentsView.as_view()),
    path("posts/comments/<int:pk>/", views.commentsView.as_view()),
    path("posts/comments/<int:pk>/", views.commentsViewDelete.as_view())
]

# TALVEZ DÊ MUITO ERRADO ASSIM, PRESTAR ATENÇÃO!!!!
