# Generated by Django 3.2.6 on 2021-08-30 07:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("apis", "0004_auto_20210830_0915"),
    ]

    operations = [
        migrations.RenameField(
            model_name="country",
            old_name="name",
            new_name="country",
        ),
        migrations.RenameField(
            model_name="hotel",
            old_name="name",
            new_name="hotel",
        ),
    ]
