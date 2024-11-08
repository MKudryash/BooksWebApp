# Generated by Django 4.1.4 on 2024-11-06 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BooksWeb', '0002_alter_books_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameUser', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('feedback', models.CharField(max_length=500)),
            ],
        ),
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
