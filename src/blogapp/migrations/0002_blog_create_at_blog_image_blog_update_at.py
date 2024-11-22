# Generated by Django 5.1.2 on 2024-11-22 11:22

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="create_at",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blog",
            name="image",
            field=models.ImageField(default="", upload_to="blog_images/"),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="blog",
            name="update_at",
            field=models.DateTimeField(auto_now=True),
        ),
    ]
