# Generated by Django 4.2.2 on 2023-06-23 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dashboard', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='food_item',
            name='description',
            field=models.TextField(default=1, max_length=600),
            preserve_default=False,
        ),
    ]
