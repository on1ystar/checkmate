# Generated by Django 3.0.8 on 2020-10-03 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0004_auto_20201001_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='timer',
            field=models.DurationField(blank=True, default=300),
        ),
    ]
