# Generated by Django 4.2.11 on 2024-04-25 22:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('static_pages', '0002_contactform'),
    ]

    operations = [
        migrations.AddField(
            model_name='flan',
            name='price',
            field=models.FloatField(default=0.0),
        ),
    ]
