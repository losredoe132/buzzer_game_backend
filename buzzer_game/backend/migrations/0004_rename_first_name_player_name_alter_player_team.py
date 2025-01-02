# Generated by Django 5.1.4 on 2025-01-02 18:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("backend", "0003_rename_name_player_first_name_alter_player_team"),
    ]

    operations = [
        migrations.RenameField(
            model_name="player",
            old_name="first_name",
            new_name="name",
        ),
        migrations.AlterField(
            model_name="player",
            name="team",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="players",
                to="backend.team",
            ),
        ),
    ]
