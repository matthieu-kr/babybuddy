# Generated by Django 2.2 on 2019-05-02 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0005_auto_20190416_2048"),
    ]

    operations = [
        migrations.AlterField(
            model_name="feeding",
            name="method",
            field=models.CharField(
                choices=[
                    ("bottle", "Bottle"),
                    ("left breast", "Left breast"),
                    ("right breast", "Right breast"),
                    ("both breasts", "Both breasts"),
                ],
                max_length=255,
                verbose_name="Method",
            ),
        ),
    ]
