# Generated by Django 4.2 on 2023-06-14 15:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0004_rename_by_mock_trainers'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mock',
            old_name='Trainers',
            new_name='by',
        ),
    ]