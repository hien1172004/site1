# Generated by Django 5.1.2 on 2024-11-07 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_alter_book_id_alter_student_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
