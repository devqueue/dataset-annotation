# Generated by Django 4.0.2 on 2022-11-23 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ner',
            name='tag',
            field=models.TextField(),
        ),
    ]
