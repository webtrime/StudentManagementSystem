# Generated by Django 4.1.4 on 2022-12-21 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_remove_users_roll_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='roll_no',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='users',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]