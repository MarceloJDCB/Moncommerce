from django.test import TestCase
from .serializers import ProductSerializer

class StoreTestCase(TestCase):
    def test_serializer(self):
        # true
        product_serializer = ProductSerializer(data=self.product)
        self.assertTrue(product_serializer.is_valid())
        
        # false
        false_product = self.product
        false_product['image'] = 'zxf'
        product_serializer = ProductSerializer(data=false_product)
        self.assertFalse(product_serializer.is_valid())
        
        
    
    @property
    def product(self):
        product = {'name':'test',
                'description':'test',
                'price':10.10,
                'image':'',
                'supply':1}
        return product

# Create your tests here.
