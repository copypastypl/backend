# Generated by Django 3.2 on 2021-05-22 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_auto_20210509_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default='2021-05-22T19:28:30'),
            preserve_default=False,
        ),
    ]
