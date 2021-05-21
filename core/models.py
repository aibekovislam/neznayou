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


    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"


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


    class Meta:
        verbose_name = "Аккаунт"
        verbose_name_plural = "Аккаунты"

    def __str__(self):
        return self.acc


class AboutUs(models.Model):
    title = models.CharField(max_length=250)
    text = models.TextField()
    img = models.ImageField(upload_to="Image_About_Us", blank=True, null=True, verbose_name="Картинка о нас")


    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"

    def __str__(self):
        return self.title


class ContactUs(models.Model):
    name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=90)


    class Meta:
        verbose_name = 'Связи и контакты'
        verbose_name_plural = 'Связи и контакты'


    def __str__(self):
        return self.name
    
    

