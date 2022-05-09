# Generated by Django 4.0.4 on 2022-05-08 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=400)),
                ('designation', models.CharField(max_length=200)),
                ('image_50_by_50', models.ImageField(blank=True, null=True, upload_to='')),
                ('testimony', models.TextField(blank=True, null=True)),
                ('rating', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(choices=[('', '---------'), ('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Team',
                'verbose_name_plural': 'Team',
            },
        ),
    ]
