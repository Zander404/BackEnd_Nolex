# Generated by Django 4.2.3 on 2023-08-03 12:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='')),
                ('description', models.TextField(default='', max_length=400, null=True)),
                ('iniciate', models.DateField()),
                ('conclusion', models.DateField(blank=True)),
                ('link', models.CharField(blank=True, default='', null=True)),
                ('image', models.ImageField(blank=True, upload_to='media/skill/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='')),
                ('description', models.TextField(default='', max_length=400, null=True)),
                ('categorie', models.CharField(choices=[(1, 'front'), (2, 'back')], default='back')),
                ('image', models.ImageField(blank=True, upload_to='media/skill/')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['created'],
            },
        ),
    ]
