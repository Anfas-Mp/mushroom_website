# Generated by Django 4.2.2 on 2023-09-01 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mushroom_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='desc',
            field=models.TextField(default=300),
            preserve_default=False,
        ),
    ]
