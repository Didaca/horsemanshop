from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from horsemanshop.shop.models import Article, Category
from horsemanshop.shop.serializers import ArticleSerializer, CategorySerializer, ArticleForListSerializer


class ArticleListView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleForListSerializer

    def list(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        serializer = ArticleForListSerializer(queryset, many=True)

        return Response(serializer.data)


class ArticleDetailsView(APIView):

    def get_object(self, pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleCreateView(CreateAPIView):

    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(ListAPIView):
    queryset = Category.objects.all().prefetch_related('article_set')
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)


class CategoryCreateView(APIView):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
