# Generated by Django 4.2.1 on 2023-07-07 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0019_stator_next_change"),
    ]

    operations = [
        migrations.AlterField(
            model_name="identity",
            name="local",
            field=models.BooleanField(db_index=True),
        ),
    ]
