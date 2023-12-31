# Generated by Django 4.2 on 2023-06-14 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HR', '0002_student_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='name')),
                ('pno', models.CharField(max_length=50, verbose_name='pno')),
                ('email', models.CharField(max_length=50, verbose_name='email')),
                ('subject', models.CharField(max_length=50, verbose_name='subject')),
                ('comm', models.CharField(max_length=50, verbose_name='Communication rating')),
                ('tech', models.CharField(max_length=50, verbose_name='technical rating')),
                ('prog', models.CharField(max_length=50, verbose_name='Programming rating')),
                ('date', models.CharField(max_length=50, verbose_name='Conducted on')),
                ('by', models.CharField(max_length=50, verbose_name='Conducted by')),
            ],
        ),
    ]
