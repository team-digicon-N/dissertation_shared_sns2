# Generated by Django 3.2 on 2021-09-08 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0011_boardmodel_article_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='article_urls',
            field=models.URLField(blank=True, null=True),
        ),
    ]
