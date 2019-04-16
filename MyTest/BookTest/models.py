from django.db import models

# Create your models here.


class Book(models.Model):
    btitle = models.CharField(max_length=20)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.btitle


class Hero(models.Model):
    name = models.CharField(max_length=20)
    gender = models.BooleanField()
    content = models.CharField(max_length=50)
    book = models.ForeignKey("Book", on_delete=models.CASCADE)

    def __str__(self):
        return self.name



