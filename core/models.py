from django.db import models
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0,validators=[MaxValueValidator(5)])
    picture = models.ImageField(upload_to="product_image", blank=True, null=True, verbose_name="Картинка продукта")
    is_active = models.BooleanField(default=True)


    def __str__(self):
        return self.title



class Users(models.Model):
    acc = models.OneToOneField(
        to=User,
        related_name='Account',
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Аккаунт"
    )

    def __str__(self):
        return self.acc

