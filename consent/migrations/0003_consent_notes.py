# Generated by Django 2.0.3 on 2018-05-23 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consent', '0002_auto_20180523_1154'),
    ]

    operations = [
        migrations.AddField(
            model_name='consent',
            name='notes',
            field=models.TextField(blank=True, help_text='You can use this to keep notes of how the consent was granted, such as the actual text that was used to ask for consent.'),
        ),
    ]
