from django.urls import path

from horsemanshop.shop.views import ArticleListView, CategoryListView, ArticleCreateView, ArticleDetailsView, \
    ArticleUpdateDeleteView

urlpatterns = [
    path('articles/', ArticleListView.as_view(), name='articles'),
    path('create-article/', ArticleCreateView.as_view(), name='create_article'),
    path('article/<int:pk>/', ArticleDetailsView.as_view(), name='details'),
    path('article-up-del/<int:pk>/', ArticleUpdateDeleteView.as_view(), name='up_del'),

    path('categories/', CategoryListView.as_view(), name='all_categories'),
]
