from django.urls import path
from .views import FirePostView

urlpatterns = [
    path("fire/posts/<int:post_id>/", FirePostView.as_view())
]