from django.db import models

# Create your models here.

class CredsModel(models.Model):
    server = models.CharField(max_length=100, default = "", null=True)
    email = models.EmailField()
    api_token = models.CharField(max_length=100)
    
class CardDataModel(models.Model):
    
    email = models.EmailField()
    num_cards = models.IntegerField()
