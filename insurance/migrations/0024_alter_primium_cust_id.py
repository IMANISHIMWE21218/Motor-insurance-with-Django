# Generated by Django 4.1.4 on 2022-12-21 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("insurance", "0023_alter_primium_cust_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="primium",
            name="cust_id",
            field=models.CharField(default="cust73016", max_length=70),
        ),
    ]
