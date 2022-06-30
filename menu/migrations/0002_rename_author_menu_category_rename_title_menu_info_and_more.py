# Generated by Django 4.0.5 on 2022-06-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='author',
            new_name='category',
        ),
        migrations.RenameField(
            model_name='menu',
            old_name='title',
            new_name='info',
        ),
        migrations.AddField(
            model_name='menu',
            name='name',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='menu',
            name='price',
            field=models.CharField(default=255, max_length=255),
            preserve_default=False,
        ),
    ]
