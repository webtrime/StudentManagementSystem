# Generated by Django 2.2.28 on 2022-12-21 17:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20221221_1747'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='roll_no',
        ),
    ]
