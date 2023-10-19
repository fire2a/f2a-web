from django.db import models
from datetime import date

# Create your models here.
class Offer(models.Model):
    name = models.TextField(max_length=300)
    description = models.TextField()
    pub_date = models.DateField(default=date.today)
    payed = models.BooleanField(default=False)
    pay = models.IntegerField(blank=True, default=0, )
    project = models.ManyToManyField('project.Project', blank=True, related_name="offers")
    DOCTORAL_STUDENT = 'PHD'
    MASTER_STUDENT = 'MG'
    UG_STUDENT = 'UG'
    POSTDOCTORATE = 'PPHD'
    RESEARCH_ASSISTANT = 'RA'
    RESEARCHER = 'R'
    OFFER_CHOICES = [
        (DOCTORAL_STUDENT, 'Phd'),
        (UG_STUDENT, 'Undergraduate'),
        (MASTER_STUDENT, 'Master'),
        (POSTDOCTORATE, 'Postdoc'),
        (RESEARCH_ASSISTANT, 'Research Assistant'),
        (RESEARCHER, 'Researcher'),
    ]
    offer_type = models.CharField(choices=OFFER_CHOICES, max_length=100)
    contact_mail = models.EmailField(max_length=200)
    contact_phone = models.CharField(max_length=100)
    OPEN = 'O'
    CLOSED = 'C'
    UNPUBLISHED = 'U' 
    STATUS_CHOICES = [
        (OPEN, 'open'),
        (CLOSED, 'closed'),
        (UNPUBLISHED, 'unpublished'),
    ] 
    offer_status = models.CharField(choices=STATUS_CHOICES, max_length=100, default=UNPUBLISHED)
    
    def __str__(self):
        return self.name