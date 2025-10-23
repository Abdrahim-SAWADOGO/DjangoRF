from rest_framework.viewsets import ModelViewSet
from rest_framework.viewsets import ReadOnlyModelViewSet

from shop.models import Category, Article, Product

from shop.serializers import CategorySerializer, ArticleSerializer, ProductSerializer


class CategoryViewset(ReadOnlyModelViewSet):

    serializer_class = CategorySerializer

    def get_queryset(self):
        return Category.objects.all()
    

class ProductViewset(ModelViewSet):

    serializer_class = ProductSerializer

    def get_queryset(self):
        # recuperer les produits actifs et optionnellement par categorie
        queryset = Product.objects.filter(active=True)
        category_id=self.request.GET.get('category_id')
        if category_id is not None:
            queryset = queryset.filter(category_id=category_id)
        return queryset
    

class ArticleViewset(ModelViewSet):

    serializer_class = ArticleSerializer

    def get_queryset(self):
        return Article.objects.filter(active=True)

