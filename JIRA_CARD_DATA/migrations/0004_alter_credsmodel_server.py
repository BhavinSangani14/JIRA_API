# Generated by Django 4.1.5 on 2023-04-01 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("JIRA_CARD_DATA", "0003_credsmodel_server"),
    ]

    operations = [
        migrations.AlterField(
            model_name="credsmodel",
            name="server",
            field=models.CharField(max_length=100),
        ),
    ]
