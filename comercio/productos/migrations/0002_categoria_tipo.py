# Generated by Django 4.2.5 on 2023-09-11 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoria',
            name='tipo',
            field=models.CharField(max_length=100, null=True),
        ),
    ]