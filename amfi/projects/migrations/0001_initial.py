# Generated by Django 4.0.4 on 2022-05-08 20:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=400)),
                ('slug', models.SlugField(max_length=200)),
                ('image_570_by_640', models.ImageField(blank=True, null=True, upload_to='')),
                ('amount_required', models.PositiveIntegerField(default=0)),
                ('amount_raised', models.PositiveIntegerField(default=0)),
                ('percentage', models.PositiveIntegerField(default=0)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image_770_by_445', models.ImageField(blank=True, null=True, upload_to='')),
                ('sub_title2', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_body2', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('', '---------'), ('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('supervisor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='project_owner', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-id'],
            },
        ),
    ]
