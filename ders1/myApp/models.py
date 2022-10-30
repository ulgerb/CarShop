from django.db import models
from django.contrib.auth.models import User


# Create your models here.


class Post(models.Model):
    title = models.CharField(("Başlık"), max_length=50)
    text = models.TextField(("Post Yazısı"))
    image = models.FileField(("Post Fotoğrafı"), upload_to='post')
    new_date = models.DateTimeField(("Paylaşma tarihi"),  auto_now_add=True)
    fiyat = models.IntegerField(('Fiyat'))
    
    def __str__(self) -> str:
        return self.title

class Shop(models.Model):
    user = models.ForeignKey(User, verbose_name=(""), on_delete=models.CASCADE)
    product = models.ForeignKey(Post, verbose_name=("Ürün Adı"), on_delete=models.CASCADE)
    fiyat = models.IntegerField(("Ürün Fiyatı"))
    adet = models.IntegerField(("Ürün Adeti"))
    image = models.FileField(("Ürün Foroğrafı"), upload_to='post')
    
    def __str__(self) -> str:
        return self.product.title


class UserSave(models.Model):
    user = models.CharField(("Kullanıcı adı"), max_length=200)
    password = models.CharField(("Kullanıcı Şifre"), max_length=200)

    def __str__(self) -> str:
        return self.user
