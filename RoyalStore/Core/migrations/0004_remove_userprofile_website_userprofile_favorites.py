# Generated by Django 4.2.4 on 2023-12-11 17:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("Core", "0003_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="userprofile",
            name="website",
        ),
        migrations.AddField(
            model_name="userprofile",
            name="favorites",
            field=models.ManyToManyField(blank=True, to="Core.productos"),
        ),
    ]
