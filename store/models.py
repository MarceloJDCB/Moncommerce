from unicodedata import decimal
from django.db import models

import base64

class Product(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=5,decimal_places=2)
    image = models.FileField(upload_to='imgs')
    supply = models.IntegerField()

    @property
    def frame_url(self):
        return self.image
    
    @property
    def frame_base64(self):
        path = "media/" + str(self.image)
        try:
            with open(path, 'rb') as f:
                content = f.read()
            img = (base64.b64encode(content))
        except:
            img = ("Imagem não encontrada no nosso banco de dados...")
        return img

    @property
    def frame_html_base64(self):
        path = "media/" + str(self.image)
        try:
            with open(path, 'rb') as f:
                content = f.read()
            img = "data:image/png;base64," + (base64.b64encode(content)).decode()
        except:
            img = ("Imagem não encontrada no nosso banco de dados...")
        return img
    
#data:image/jpeg;base64
# Create your models here.
