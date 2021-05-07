from django.db import models

# Create your models here.
class Products(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=150)
    date = models.DateTimeField(auto_now_add=True, null=True)


    def __str__(self):
        return self.title

