# Generated by Django 5.0.2 on 2024-02-24 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lead', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='lead',
            name='converted_to_client',
            field=models.BooleanField(default=False),
        ),
    ]
