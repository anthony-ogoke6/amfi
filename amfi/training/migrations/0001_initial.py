# Generated by Django 4.0.4 on 2022-05-09 19:44

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
            name='Training',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(blank=True, max_length=200, null=True)),
                ('title', models.CharField(blank=True, max_length=400, null=True)),
                ('slug', models.SlugField(blank=True, max_length=200, null=True)),
                ('image_570_by_640', models.ImageField(blank=True, null=True, upload_to='')),
                ('amount_required', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('amount_raised', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('percentage', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('sub_title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('image_770_by_445', models.ImageField(blank=True, null=True, upload_to='')),
                ('sub_title2', models.CharField(blank=True, max_length=200, null=True)),
                ('sub_body2', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('', '---------'), ('draft', 'Draft'), ('published', 'Published')], max_length=10)),
                ('view_count', models.PositiveIntegerField(default=0)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('facilitator', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='training_facilitator', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Project',
                'verbose_name_plural': 'Projects',
                'ordering': ['-id'],
            },
        ),
    ]