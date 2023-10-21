# Generated by Django 4.1.4 on 2023-10-03 11:50

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('researcher', '0012_alter_researcher_position'),
    ]

    operations = [
        migrations.AlterField(
            model_name='researcher',
            name='photo',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, quality=-1, scale=None, size=[500, 300], upload_to='img/researchers/'),
        ),
    ]