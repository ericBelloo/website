# Generated by Django 2.2.2 on 2020-02-03 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('model', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='documents',
            name='departmental',
            field=models.SmallIntegerField(blank=True, null=True),
        ),
    ]