# Generated by Django 5.0.2 on 2024-03-03 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App1', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagemodel',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]