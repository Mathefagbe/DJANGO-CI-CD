# Generated by Django 5.2 on 2025-04-26 12:52

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app_portfolio", "0002_alter_experience_experience"),
    ]

    operations = [
        migrations.AddField(
            model_name="workexperience",
            name="project",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="app_portfolio.projects",
            ),
        ),
    ]
