# Generated by Django 4.2.16 on 2024-09-19 07:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='questions',
            new_name='question',
        ),
    ]