from django.db import models

# Create your models here.
class CardData(models.Model):
    
    Issue_Type = models.CharField(max_length=20)
    Project = models.CharField(max_length=20)
    Time_Spent = models.CharField(max_length=20)
    Status = models.CharField(max_length=20)
    Story_Points = models.CharField(max_length=5)
    Last_Viewed = models.CharField(max_length=20)
    Sprint = models.CharField(max_length=20)
    Priority = models.CharField(max_length=20)
    Assignee = models.CharField(max_length = 20)
    Issue_Key = models.CharField(max_length=20)
    Description = models.CharField(max_length=50)
    Summary = models.TextField()
    Reporter = models.CharField(max_length=20)
    
    def __str__(self):
        return self.Issue_Key
    
