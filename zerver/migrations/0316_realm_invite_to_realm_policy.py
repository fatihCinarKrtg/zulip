# Generated by Django 3.1.7 on 2021-04-01 19:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("zerver", "0315_realmplayground"),
    ]

    operations = [
        migrations.AddField(
            model_name="realm",
            name="invite_to_realm_policy",
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]