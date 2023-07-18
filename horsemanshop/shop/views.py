from django.http import Http404
from rest_framework import status
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.views import APIView

from horsemanshop.shop.mixins import IsAuthenticatedOrReadOnlyPermissionsMixin, IsOwnerPermissionsMixin,\
    IsAuthenticatedPermissionsMixin
from horsemanshop.shop.models import Article, Category
from horsemanshop.shop.serializers import ArticleSerializer, CategorySerializer, ArticleForListSerializer, \
    CreateArticleSerializer


class ArticleListView(
    IsAuthenticatedOrReadOnlyPermissionsMixin,
    ListAPIView
):

    queryset = Article.objects.all()
    serializer_class = ArticleForListSerializer

    def list(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        serializer = ArticleForListSerializer(queryset, many=True)

        return Response(serializer.data)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class ArticleDetailsView(
    IsAuthenticatedOrReadOnlyPermissionsMixin,
    APIView
):

    @staticmethod
    def get_object(pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)


class ArticleUpdateDeleteView(
    IsOwnerPermissionsMixin,
    APIView
):

    @staticmethod
    def get_object(pk):
        try:
            return Article.objects.get(pk=pk)
        except Article.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        article = self.get_object(pk)
        serializer = ArticleSerializer(article, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        article = self.get_object(pk)
        article.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)


class ArticleCreateView(
    IsAuthenticatedPermissionsMixin,
    CreateAPIView
):

    queryset = Article.objects.all()
    serializer_class = CreateArticleSerializer

    def get(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        serializer = ArticleSerializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = CreateArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CategoryListView(
    IsAuthenticatedOrReadOnlyPermissionsMixin,
    ListAPIView
):

    queryset = Category.objects.all().prefetch_related('article_set')
    serializer_class = CategorySerializer

    def list(self, request, *args, **kwargs):
        queryset = super().get_queryset()
        serializer = CategorySerializer(queryset, many=True)

        return Response(serializer.data)
