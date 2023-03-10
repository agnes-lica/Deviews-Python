from rest_framework.views import APIView, Request, Response, status
from django.shortcuts import get_object_or_404
from .serializers import FirePostSerializer, FireCommentSerializer
from posts.models import Post
from comments.models import Comment
from users.permissions import IsAccountOwnerOrdAdm
from rest_framework_simplejwt.authentication import JWTAuthentication



class FirePostView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    def post(self, request: Request, post_id: int) -> Response:
        request.data["post"] = post_id
        request.data["user"] = request.user.id
        serializer = FirePostSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if not serializer.data["exists"]:
            return Response({"message": "Desfire"}, status.HTTP_201_CREATED)

        return Response({"message": "Fire"}, status.HTTP_201_CREATED)

class FireCommentsView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAccountOwnerOrdAdm]

    def post(self, request: Request, comment_id: int) -> Response:
        request.data["comment"] = comment_id
        request.data["user"] = request.user.id
        serializer = FireCommentSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        if not serializer.data["exists"]:
            return Response({"message": "Desfire"}, status.HTTP_201_CREATED)

        return Response({"message": "Fire"}, status.HTTP_201_CREATED)