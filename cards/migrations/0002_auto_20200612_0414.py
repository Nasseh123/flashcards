# Generated by Django 3.0.7 on 2020-06-12 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cards', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank=True, default='male.png', upload_to='profile/'),
        ),
    ]