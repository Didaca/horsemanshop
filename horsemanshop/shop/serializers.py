from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator

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
            'category'
        ]
        validators = [
            UniqueTogetherValidator(
                queryset=Article.objects.all(),
                fields=['name', 'article_type'],
                message='The relation name-type already exist!'
            )
        ]

    @staticmethod
    def validate_name(name):
        art = Article.objects.filter(name__iexact=name)
        if art.exists():
            raise serializers.ValidationError(f'{name} is already exist!')
        return name


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
