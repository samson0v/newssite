# Generated by Django 3.0.3 on 2020-02-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0008_remove_news_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.CharField(default='vitalikbidochka@gmail.com', max_length=200),
            preserve_default=False,
        ),
    ]