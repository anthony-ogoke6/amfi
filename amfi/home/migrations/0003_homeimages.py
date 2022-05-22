# Generated by Django 3.2 on 2022-05-21 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_home_reference'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomeImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('', '---------'), ('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('image_big', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_small_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('image_small_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'HomeImage',
                'verbose_name_plural': 'Home Images',
                'ordering': ['-id'],
            },
        ),
    ]