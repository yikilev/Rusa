# Generated by Django 4.1.6 on 2024-05-23 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Constructor', '0004_remove_line_seasons_delete_season_line_seasons'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='notes',
            field=models.TextField(null=True),
        ),
    ]
