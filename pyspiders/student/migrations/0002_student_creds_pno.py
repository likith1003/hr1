# Generated by Django 4.2 on 2023-06-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student_creds',
            name='pno',
            field=models.CharField(default='', max_length=50, verbose_name='pno'),
            preserve_default=False,
        ),
    ]
