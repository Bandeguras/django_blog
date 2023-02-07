from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from webapp.models import Comment
from api_v1.serializers import CommentSerializer


class CommentView(APIView):
    def get(self, request, *args, **kwargs):
        comments = Comment.objects.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CommentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class CommentViewPK(APIView):
    def put(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        serializer = CommentSerializer(data=request.data, instance=comment)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        serializer = CommentSerializer(comment)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        comment = get_object_or_404(Comment, pk=kwargs.get('pk'))
        comment_pk = comment.pk
        comment.delete()
        return Response({
            "message": f"Comment with id {comment_pk} has been deleted."
        }, status=204)
