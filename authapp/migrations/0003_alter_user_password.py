# Generated by Django 4.1.1 on 2022-10-10 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authapp", "0002_alter_user_managers_alter_user_password"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=64),
        ),
    ]
