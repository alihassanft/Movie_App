# Generated by Django 4.2.11 on 2024-05-06 15:44

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_movierating'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='movierating',
            unique_together=set(),
        ),
        migrations.AddField(
            model_name='movierating',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 5, 6, 15, 44, 46, 237202, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movierating',
            name='movie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ratings', to='api.movie'),
        ),
        migrations.AlterField(
            model_name='movierating',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
