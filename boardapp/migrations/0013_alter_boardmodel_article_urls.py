# Generated by Django 3.2 on 2021-09-08 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('boardapp', '0012_alter_boardmodel_article_urls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='boardmodel',
            name='article_urls',
            field=models.CharField(blank=True, default=0, max_length=200, null=True),
        ),
    ]
