# Generated by Django 4.1.6 on 2024-06-04 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Userprofile', '0008_alter_userprofile_personal_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='personal_photo',
            field=models.ImageField(default='default/anon.png', upload_to='profile_photos/'),
        ),
    ]
