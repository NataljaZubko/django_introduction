# Generated by Django 5.0.7 on 2024-08-01 08:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0005_publisher_book_publisher_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='book',
            old_name='publisher_id',
            new_name='publisher',
        ),
    ]
