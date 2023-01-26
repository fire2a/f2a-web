from django.db import models
from datetime import date

# Create your models here.
class Project(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField(max_length=300)
    date = models.DateField(default=date.today)
    link = models.URLField(blank=True)
    participants = models.ManyToManyField('researcher.Researcher', blank=True, related_name="projects")
    research_lines = models.ManyToManyField('research.Research', blank=True, related_name="projects")
    papers = models.ManyToManyField('paper.Paper', blank=True, related_name="projects")

    def __str__(self):
        return self.name