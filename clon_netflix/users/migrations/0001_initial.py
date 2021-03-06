# Generated by Django 3.1 on 2021-01-19 21:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserM',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=50, unique=True)),
                ('title', models.TextField(max_length=60)),
                ('picture', models.ImageField(upload_to='users/pictures')),
                ('website', models.URLField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
