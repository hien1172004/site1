# Generated by Django 5.1.2 on 2024-11-17 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0017_book_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='title',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
