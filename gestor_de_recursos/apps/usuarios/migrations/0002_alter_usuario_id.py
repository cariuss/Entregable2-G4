# Generated by Django 5.2 on 2025-05-30 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
