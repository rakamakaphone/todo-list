# Generated by Django 4.2 on 2023-05-05 15:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("app", "0002_alter_task_options"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="tags",
            field=models.ManyToManyField(
                blank=True, null=True, related_name="tasks", to="app.tag"
            ),
        ),
    ]
