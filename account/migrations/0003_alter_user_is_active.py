# Generated by Django 5.0.3 on 2024-03-11 18:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_rename_created_user_created_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]