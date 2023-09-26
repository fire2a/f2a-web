from django.db import models
from datetime import date

# Create your models here.
class Paper(models.Model):
    title = models.TextField(max_length=300)
    abstract = models.TextField()
    date = models.DateField(default=date.today)
    file = models.FileField(upload_to='papers/', blank=True)
    link = models.URLField(blank=True)
    JOURNAL = 'JRN'
    PRESENTATION = 'PRST'
    CONFERENCE = 'CON'
    THESIS = 'TH'
    CHAPTER = 'CH'
    PUBLICATION_CHOICES = [
        (JOURNAL, 'Journal'),
        (PRESENTATION, 'Presentation'),
        (CONFERENCE, 'Conference'),
        (THESIS, 'Thesis'),
        (CHAPTER, 'Chapter'),
    ]
    type = models.CharField(choices=PUBLICATION_CHOICES, max_length=100)
    authors = models.ManyToManyField('researcher.Researcher', blank=True, related_name="papers")
    topic = models.ManyToManyField('research.Research', blank=True, related_name="papers")

    def __str__(self):
        return self.title