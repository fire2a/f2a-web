# Generated by Django 4.1.4 on 2023-09-25 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offers', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='pay',
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
