# Generated by Django 2.2.3 on 2019-07-25 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0018_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='date',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]