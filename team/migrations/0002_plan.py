# Generated by Django 5.0.2 on 2024-03-07 20:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('team', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('description', models.TextField(blank=True, null=True)),
                ('max_leads', models.IntegerField()),
                ('max_clients', models.IntegerField()),
            ],
        ),
    ]