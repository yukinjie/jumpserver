# Generated by Django 3.1.6 on 2021-07-01 05:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0035_auto_20210526_1100'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'default_permissions': [], 'ordering': ['username'], 'permissions': [('Create user', 'Create user'), ('Update user', 'Update user'), ('Delete user', 'Delete user'), ('View user', 'View user')], 'verbose_name': 'User'},
        ),
    ]