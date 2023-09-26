# Generated by Django 4.1.4 on 2023-09-25 09:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0002_offer_pay'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='offer_status',
            field=models.CharField(choices=[('O', 'open'), ('C', 'closed'), ('U', 'unpublished')], default='unpublished', max_length=100),
        ),
    ]