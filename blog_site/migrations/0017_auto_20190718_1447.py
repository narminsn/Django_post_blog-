# Generated by Django 2.2.3 on 2019-07-18 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0016_postmodel_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='subtitle',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]
