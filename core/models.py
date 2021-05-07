from django.db import models
from django.core.validators import MaxValueValidator

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True, null=True)
    rating = models.IntegerField(null=True, blank=True, default=0,validators=[MaxValueValidator(5)])


    def __str__(self):
        return self.title

