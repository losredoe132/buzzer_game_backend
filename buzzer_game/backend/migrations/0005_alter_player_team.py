# Generated by Django 5.1.4 on 2025-01-05 08:17

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0004_rename_first_name_player_name_alter_player_team"),
    ]

    operations = [
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="players",
                to="backend.team",
            ),
        ),
    ]