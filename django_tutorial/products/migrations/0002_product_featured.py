# Generated by Django 4.2.16 on 2024-09-14 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("products", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="product",
            name="featured",
            field=models.BooleanField(default=False, null=True),
        ),
    ]
