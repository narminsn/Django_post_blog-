# Generated by Django 2.2.3 on 2019-07-17 14:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0014_auto_20190717_1003'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='background_image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]