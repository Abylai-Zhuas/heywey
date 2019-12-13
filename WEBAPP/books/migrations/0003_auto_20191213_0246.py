# Generated by Django 3.0 on 2019-12-12 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_book_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_content',
            field=models.FileField(default='NULL', upload_to='media'),
        ),
        migrations.AlterField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='NULL', upload_to='media'),
        ),
    ]