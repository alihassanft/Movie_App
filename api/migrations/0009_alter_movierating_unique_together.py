# Generated by Django 4.2.11 on 2024-05-06 16:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_movierating_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movierating',
            unique_together={('movie', 'user')},
        ),
    ]
