# Generated by Django 2.2.16 on 2022-12-15 14:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_auto_20221215_1729'),
    ]

    operations = [
        migrations.RenameField(
            model_name='follow',
            old_name='author',
            new_name='user',
        ),
    ]
