# Generated by Django 3.2 on 2022-05-12 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('enroll', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='enroll',
            old_name='description',
            new_name='address',
        ),
        migrations.RenameField(
            model_name='enroll',
            old_name='support_line',
            new_name='phone_number',
        ),
    ]
