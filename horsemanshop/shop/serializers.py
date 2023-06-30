from rest_framework import serializers

from horsemanshop.shop.models import Article, Category


class CategoryForArticleSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']


class ArticleForListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Article
        fields = ['id', 'name']


class ArticleSerializer(serializers.ModelSerializer):

    category = CategoryForArticleSerializer(many=False)

    class Meta:
        model = Article
        fields = "__all__"


class CategorySerializer(serializers.ModelSerializer):

    article_set = ArticleForListSerializer(many=True)

    class Meta:
        model = Category
        fields = "__all__"
