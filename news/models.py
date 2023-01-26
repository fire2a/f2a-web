from django.db import models
from datetime import date
# Create your models here.
class News(models.Model):
    title = models.TextField(max_length=300)
    description = models.TextField()
    link = models.URLField()
    image = models.ImageField(upload_to='img/news/', blank=True)
    featured = models.BooleanField(default=False)
    mentioned = models.ManyToManyField('researcher.Researcher', blank=True, related_name="news")
    projects = models.ManyToManyField('project.Project', blank=True, related_name="news")
    research_lines = models.ManyToManyField('research.Research', blank=True, related_name="news")
    related_news = models.ManyToManyField('self', blank=True)
    date = models.DateField(default=date.today)
    def __str__(self) -> str:
        return self.title