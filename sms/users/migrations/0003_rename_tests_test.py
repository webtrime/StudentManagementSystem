# Generated by Django 4.1.4 on 2023-01-07 02:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_tests_testtype_remove_practicalinternalstudent_s_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tests',
            new_name='Test',
        ),
    ]