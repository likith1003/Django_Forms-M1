from django.db import models

# Create your models here.

class Customer(models.Model):
    cid = models.IntegerField(primary_key=True)
    cname = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    pno = models.CharField(max_length=50)
    un = models.CharField(max_length=50)
    pw = models.CharField(max_length=50)

    def __str__(self):
        return self.cname