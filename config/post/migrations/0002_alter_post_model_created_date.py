# Generated by Django 5.0.2 on 2024-02-27 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post_model',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
