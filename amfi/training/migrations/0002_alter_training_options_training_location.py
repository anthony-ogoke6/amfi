# Generated by Django 4.0.4 on 2022-05-11 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='training',
            options={'ordering': ['-id'], 'verbose_name': 'Training', 'verbose_name_plural': 'Training'},
        ),
        migrations.AddField(
            model_name='training',
            name='location',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
