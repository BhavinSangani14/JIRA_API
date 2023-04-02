from django.contrib import admin
from .models import CardData
# Register your models here.

class Card_Data(admin.ModelAdmin):
    
    list_display = ("Issue_Type", "Project", "Time_Spent", "Status", "StoryPoints", "Last_Viewed", "Sprint", "Priority", "Assignee", 'Issue_Key', "Description", "Summary", "Reporter")

admin.site.register(CardData)