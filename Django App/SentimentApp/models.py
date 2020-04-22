from django.db import models

class SentimentModel(models.Model):
    Sentence = models.CharField(max_length=120)
    
