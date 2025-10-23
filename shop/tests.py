from django.urls import reverse_lazy
from rest_framework.test import APITestCase

from .models import Category, Product, Article


class TestCategory(APITestCase):
    
    #Nous stockons l'url de l'endpoint dans un attribut de claase pour pouvoir l'utiliser facilement dans chacun nos tests
    url=reverse_lazy('category-list')

    def format_datetime(self, value):
        # Cette methode est helpper permettant de formater un datetime en string
        return value.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    def test_list(self):
        #creons deux catégories dont une seule est active
        category=Category.objects.create(name='Fruit',active=True)
        category.objects.create(name='Légumes',active=False)

        #on realise l'appel en get en uttilisant le client de la classe APITestCase
        response=self.client.get(self.url)

        #on verifie le status code de la response et que les valeur retournees sont correctes
        self.assertEqual(response.status_code,200)
        excepted=[
            {
                'id':category.pk,
                'name':category.name,
                'date_created':self.format_datetime(category.date_created),
                'date_updated':self.format_datetime(category.date_updated),
            }
        ]
        self.assertEqual(excepted, response.json)

    def test_create(self):
        # Nous vérifions qu'aucune categorie n'existe avant de créer une nouvelle
        self.assertFalse(Category.objects.exists())
        response=self.client.post(self.url,data={'name':'Nouvelle categorie'})
        # verifier que le status code est bien en erreur et empeche la création
        self.assertEqual(response.status_code,405)
        # Enfin, vérifions qu'aucune categorie n'a ete creee malgre le status code 405
        self.assertFalse(Category.objects.exists())
        