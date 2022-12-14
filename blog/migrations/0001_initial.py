# Generated by Django 4.1 on 2022-09-05 15:57

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('excerpt', models.TextField(null=True)),
                ('content', models.TextField()),
                ('published', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('published', 'Published'), ('draft', 'Draft')], default='published', max_length=10)),
                ('slug', models.SlugField(max_length=250, unique_for_date='published')),
            ],
            options={
                'ordering': ('-published',),
            },
        ),
    ]
