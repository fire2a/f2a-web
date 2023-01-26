from django.db import models


# Create your models here.
class Researcher(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField(default="")
    mail = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    DIRECTOR = 'DIR'
    INVESTIGADOR = 'INV'
    POSTDOC = "POST"
    PHD = 'PHD'
    MAGISTER = 'MG'
    PREGRADO = 'PG'
    POSITION_CHOICES = [
        (DIRECTOR, 'Director'),
        (INVESTIGADOR, 'Investigador'),
        (POSTDOC, 'Postdoc'),
        (PHD, 'Phd'),
        (MAGISTER, 'Magister'),
        (PREGRADO, 'Pregrado'),
    ]
    position = models.CharField(choices=POSITION_CHOICES, max_length=100)
    photo = models.ImageField(upload_to='img/researchers/', blank=True)
    research_line = models.ManyToManyField('research.Research', blank=True, related_name="researchers")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    google_scholar = models.URLField(blank=True)
    orcid = models.URLField(blank=True)
    def __str__(self):
        return self.name+'_'+self.last_name