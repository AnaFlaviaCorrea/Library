# Generated by Django 4.2.1 on 2023-05-03 22:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='books',
            old_name='director',
            new_name='author',
        ),
    ]
