# Generated by Django 3.2 on 2021-09-08 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0017_alter_boardmodel_article_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='article_urls',
            field=models.TextField(),
        ),
    ]
