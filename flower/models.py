from django.db import models

# Create your models here.
class Flower(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='media_cdn')
    content = models.TextField(blank=True)
    prize = models.SmallIntegerField()
    sales = models.BooleanField()
    new_prizes = models.SmallIntegerField(blank=True, null=True)
    order_number = models.SmallIntegerField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class Home(models.Model):
    tittle = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.tittle
 
class About(models.Model):
    tittle = models.CharField(max_length=20)
    content = models.TextField()

    def __str__(self):
        return self.tittle

class Success(models.Model):
    name = models.CharField(max_length=30)
    image = models.FileField(upload_to='media_cdn')
    content = models.TextField()
    order_number = models.SmallIntegerField()

    def __str__(self):
        return self.name
    


class Contact(models.Model):
    content = models.TextField(blank=True)
    email = models.EmailField(max_length=254)
    phone = models.SmallIntegerField()
    adress = models.CharField(max_length=50)

