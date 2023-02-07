from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from webapp.models import Article
from api_v1.serializers import ArticleSerializer


class ArticleView(APIView):
    def get(self, request, *args, **kwargs):
        articles = Article.objects.all()
        serializer = ArticleSerializer(articles, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)


class ArticleViewPK(APIView):
    def put(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        serializer = ArticleSerializer(data=request.data, instance=article)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        else:
            return Response(serializer.errors, status=400)

    def get(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def delete(self, request, *args, **kwargs):
        article = get_object_or_404(Article, pk=kwargs.get('pk'))
        article_pk = article.pk
        article.delete()
        return Response({
            "message": f"Article with id {article_pk} has been deleted."
        }, status=204)
