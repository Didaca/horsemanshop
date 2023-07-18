from django.http import Http404
from django.views import generic
from rest_framework import generics, permissions

from horsemanshop.shop.models import Article, User
from horsemanshop.shop.serializers import ArticleSerializer
from horsemanshop.ui.serializers import UsersSerializer, UserSerializer, CreateUserSerializer


# demo views
class HomePageView(generic.TemplateView):
    template_name = "home.html"


class ArticleDetailsView(generic.DetailView):
    queryset = Article.objects.all()
    template_name = 'details.html'


# api views
class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = CreateUserSerializer


class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UsersSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]


class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [
        permissions.IsAdminUser
    ]


class UserArticlesListView(generics.ListAPIView):
    serializer_class = ArticleSerializer

    def get_queryset(self):

        try:
            user = self.request.user
            return Article.objects.filter(owner=user)
        except User.DoesNotExist:
            raise Http404
