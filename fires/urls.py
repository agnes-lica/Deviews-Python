from django.urls import path
from .views import FirePostView, FireCommentsView

urlpatterns = [
    path("fire/posts/<int:post_id>/", FirePostView.as_view()),
    path("fire/comments/<int:comment_id>/", FireCommentsView.as_view())
]