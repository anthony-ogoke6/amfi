# Generated by Django 4.0.4 on 2022-05-11 22:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0002_contactmessage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact',
            options={'ordering': ['-id'], 'verbose_name': 'Contact Us', 'verbose_name_plural': 'Contact Us'},
        ),
        migrations.RemoveField(
            model_name='contact',
            name='author',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='slug',
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='support_line',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]