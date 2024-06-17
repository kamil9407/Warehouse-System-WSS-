# Generated by Django 4.1.7 on 2024-04-04 12:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importwares', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='WareIdReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ware_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='importwares.addware')),
            ],
            options={
                'verbose_name_plural': 'ware_ids',
            },
        ),
    ]