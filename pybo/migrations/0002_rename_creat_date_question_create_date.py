# Generated by Django 4.0.5 on 2022-06-22 08:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='question',
            old_name='creat_date',
            new_name='create_date',
        ),
    ]
