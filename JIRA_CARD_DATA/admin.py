from django.contrib import admin
from .models import CredsModel, CardDataModel
# Register your models here.

@admin.register(CredsModel)
class Creds(admin.ModelAdmin):
    list_display = ("id", "email", "api_token")
    

@admin.register(CardDataModel)
class CardData(admin.ModelAdmin):
    list_display = ("id", "email", "num_cards")