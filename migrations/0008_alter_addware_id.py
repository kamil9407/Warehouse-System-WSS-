# Generated by Django 4.1.7 on 2024-06-05 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('importwares', '0007_alter_addware_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addware',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
