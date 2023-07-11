from django.views import generic

from horsemanshop.shop.models import Article


class HomePageView(generic.TemplateView):
    template_name = "home.html"


class ArticleDetailsView(generic.DetailView):
    queryset = Article.objects.all()
    template_name = 'details.html'
