from django.db import models

# Create your models here.
class Research(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField()
    def __str__(self):
        return self.name
    
    
