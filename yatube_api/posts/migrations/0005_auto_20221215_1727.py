# Generated by Django 2.2.16 on 2022-12-15 14:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20221215_1726'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='follow',
            name='unique_follower',
        ),
    ]
