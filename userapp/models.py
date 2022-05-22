from django.db import models
from django.contrib.auth.models import AbstractUser

USER_TYPE = (
    ('ADM', 'Administrador'),
    ('CLIENT', 'Cliente')
)

class User(AbstractUser):
    user_type = models.CharField(max_length=200, choices=USER_TYPE, verbose_name='Tipo de usuário',
                                 null=True, blank=True)
    
    cpf = models.CharField(unique=True, max_length=14, null=True, blank=True)
    
    cnpj = models.CharField(unique=True, max_length=14, null=True, blank=True)
    
    bananas = models.DecimalField(max_digits=5,decimal_places=2)
    
    def save(self, *args, **kwargs):
        response = super().save(*args, **kwargs)
        return response
# Create your models here.
