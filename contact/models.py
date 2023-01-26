from django.db import models

# Create your models here.
class Contact(models.Model):
    mail_sender = models.EmailField(max_length=200)
    subject = models.TextField(max_length=300)
    message = models.TextField()
    to = models.ManyToManyField('researcher.Researcher', related_name="messages")

    def __str__(self):
        return self.subject
