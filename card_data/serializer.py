from rest_framework import serializers
from .models import CardData

class CardDataSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CardData
        fields = "__all__"
        # fields = ("id", "Issue_Type", "Project", "Time_Spent", "Status", "StoryPoints", "Last_Viewed", "Sprint", "Priority", "Assignee", 'Issue_Key', "Description", "Summary", "Reporter")