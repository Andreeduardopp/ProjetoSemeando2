from django.db import models
from django.contrib.auth.models import AbstractUser
from utils.utils import valida_telefone

    
def get_upload_path_usuario(instance, filename):
    if not instance.id:
        return f'projetoSemeando/usuario/{filename}'
    return f'usuario/{instance.id}/{filename}'
class User(AbstractUser):
    bio = models.TextField(max_length=500, blank=True)
    celular = models.CharField(max_length=30,blank=True, validators=[valida_telefone])
    foto_perfil = models.ImageField(upload_to=get_upload_path_usuario, blank=True, null=True)
