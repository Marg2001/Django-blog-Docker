# Generated by Django 3.2.12 on 2023-10-13 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_rename_título_post_titulo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='titulo',
            new_name='título',
        ),
    ]
