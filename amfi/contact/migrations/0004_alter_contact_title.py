# Generated by Django 4.0.4 on 2022-05-11 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0003_alter_contact_options_remove_contact_author_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]