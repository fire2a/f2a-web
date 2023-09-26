# Generated by Django 4.1.4 on 2023-09-25 08:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('project', '0003_alter_project_end_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=300)),
                ('description', models.TextField()),
                ('pub_date', models.DateField(default=datetime.date.today)),
                ('payed', models.BooleanField(default=False)),
                ('offer_type', models.CharField(choices=[('PHD', 'Phd'), ('UG', 'Undergraduate'), ('MG', 'Master'), ('PPHD', 'Postdoc'), ('RA', 'Research Assistant'), ('R', 'Researcher')], max_length=100)),
                ('contact_mail', models.EmailField(max_length=200)),
                ('contact_phone', models.CharField(max_length=100)),
                ('proyect', models.ManyToManyField(blank=True, related_name='related_projects', to='project.project')),
            ],
        ),
    ]