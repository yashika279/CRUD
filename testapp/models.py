from django.db import models
class Insertion(models.Model):
    firstname=models.TextField(max_length=1000)
    lastname=models.TextField(max_length=1000)
    salary=models.CharField(max_length=30, default="" ,null=True)
    id=models.IntegerField(primary_key=True)
    def __str__(self):
        return self.id

# Create your models here.
