# Generated by Django 4.1.6 on 2024-09-21 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Constructor', '0008_group'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='preview',
            field=models.ImageField(default='previews/preview_default.jpg', upload_to='previews/'),
        ),
    ]
