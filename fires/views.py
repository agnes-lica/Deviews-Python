from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from .serializers import FirePostSerializer
from .models import FirePost
from posts.models import Post

class FirePostView(APIView):
    def post(self, request: Request, post_id: int) -> Response:
        post = get_object_or_404(Post, id=post_id)
        request.data["post"] = post
        request.data["user"] = request.user
        serializer = FirePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if not serializer.data["exists"]:
            return Response({"message": "Desfire"}, status.HTTP_201_CREATED)

        return Response({"message": "Fire"}, status.HTTP_201_CREATED)