# Generated by Django 3.0 on 2019-12-12 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20191213_0416'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Comment',
            new_name='Comments',
        ),
        migrations.RenameField(
            model_name='comments',
            old_name='comment_text',
            new_name='comments_text',
        ),
    ]
