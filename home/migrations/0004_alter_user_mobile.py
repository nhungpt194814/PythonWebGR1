# Generated by Django 4.2.1 on 2023-06-08 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_user_image_alter_user_first_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='mobile',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
