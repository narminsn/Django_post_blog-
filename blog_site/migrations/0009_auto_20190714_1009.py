# Generated by Django 2.2.3 on 2019-07-14 10:09

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog_site', '0008_headermodel_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headermodel',
            name='text',
            field=ckeditor.fields.RichTextField(blank=True, null=True),
        ),
    ]
