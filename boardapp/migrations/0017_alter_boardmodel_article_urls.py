# Generated by Django 3.2 on 2021-09-08 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0016_alter_boardmodel_article_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='article_urls',
            field=models.URLField(),
        ),
    ]
