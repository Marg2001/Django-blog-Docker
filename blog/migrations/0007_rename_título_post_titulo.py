# Generated by Django 3.2.12 on 2023-10-13 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_rename_titulo_post_título'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='título',
            new_name='titulo',
        ),
    ]
