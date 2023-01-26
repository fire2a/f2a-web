from django.db import models

# Create your models here.
class Tools(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField()
    link = models.URLField(blank=True)
    authors = models.ManyToManyField('researcher.Researcher', blank=True, related_name="tools")
    projects = models.ManyToManyField('project.Project', blank=True, related_name="tools")
    paper = models.ManyToManyField('paper.Paper', blank=True, related_name="tools")

    def __str__(self):
        return self.name