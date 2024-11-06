# Generated by Django 4.1.4 on 2024-11-06 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=100)),
                ('yearPublish', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
