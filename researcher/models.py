from django.db import models
from django_resized import ResizedImageField

# Create your models here.
class Researcher(models.Model):
    name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField(default="")
    mail = models.EmailField(max_length=200)
    phone = models.CharField(max_length=100)
    active = models.BooleanField(default=True)
    DIRECTOR = 'DIR'
    SUBDIRECTOR = 'SUBDIR'
    INVESTIGADOR_PRINCIPALES = 'INV_P'
    INVESTIGADOR_ASOCIADOS = 'INV_A'
    INVESTIGADOR_COLABORADORES = 'INV_C'
    INVESTIGADOR_EXTRANJEROS = 'INV_E'
    THESIS_UG = 'TH_UG'
    THESIS_MS = 'TH_PG'
    THESIS_PHD = 'TH_PHD'
    POSITION_CHOICES = [
        (DIRECTOR, 'Director'),
        (SUBDIRECTOR, 'Subdirector'),
        (INVESTIGADOR_PRINCIPALES, 'Investigador principal'),
        (INVESTIGADOR_ASOCIADOS, 'Investigador asociado'),
        (INVESTIGADOR_COLABORADORES, 'Investigador colaborador'),
        (INVESTIGADOR_EXTRANJEROS, 'Investigador extranjeros'),
        (THESIS_UG, 'Alumno de Pregrado'),
        (THESIS_MS, 'Alumno de Magister'),
        (THESIS_PHD, 'Alumno de Doctorado'),
    ]
    position = models.CharField(choices=POSITION_CHOICES, max_length=100)
    photo = ResizedImageField(size=[250,280], crop=['middle', 'center'], quality=100 , upload_to='img/researchers/')
    research_line = models.ManyToManyField('research.Research', blank=True, related_name="researchers")
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)
    google_scholar = models.URLField(blank=True)
    orcid = models.URLField(blank=True)
    def __str__(self):
        return self.name+'_'+self.last_name