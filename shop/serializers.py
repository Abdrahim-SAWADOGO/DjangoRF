from rest_framework.serializers import ModelSerializer
from .models import Category, Product, Article
class CategorySerializer(ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name','date_created', 'date_updated','products']


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id', 'name', 'category','date_created', 'date_updated','articles']


class ArticleSerializer(ModelSerializer):
    class Meta:
        model = Article
        fields = ['id', 'name', 'product', 'date_created', 'date_updated']