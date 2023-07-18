from django.contrib.auth import get_user_model
from rest_framework import serializers

from horsemanshop.shop.models import Article, Category


User = get_user_model()


class ArticleForListSerializer(serializers.ModelSerializer):

    category = serializers.ReadOnlyField(source='category.name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'category',
            'owner',
        ]


class CreateArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'article_type',
            'size',
            'color',
            'image',
            'price',
            'description',
            'category',
            'owner'
        ]


class ArticleSerializer(serializers.ModelSerializer):

    category = serializers.ReadOnlyField(source='category.name')
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Article
        fields = [
            'id',
            'name',
            'article_type',
            'size',
            'color',
            'image',
            'price',
            'description',
            'category',
            'owner'
        ]


class CategorySerializer(serializers.ModelSerializer):

    article_set = ArticleForListSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"
