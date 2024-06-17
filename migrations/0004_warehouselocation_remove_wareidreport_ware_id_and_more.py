# Generated by Django 4.1.7 on 2024-04-07 15:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('importwares', '0003_warewarehousereport_warepricereport_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='WarehouseLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='wareidreport',
            name='ware_id',
        ),
        migrations.RemoveField(
            model_name='wareimportquantityreport',
            name='ware_import_quantity',
        ),
        migrations.RemoveField(
            model_name='warenamereport',
            name='ware_name',
        ),
        migrations.RemoveField(
            model_name='warepricereport',
            name='ware_price',
        ),
        migrations.RemoveField(
            model_name='warewarehousereport',
            name='ware_warehouse',
        ),
        migrations.AlterModelOptions(
            name='addware',
            options={},
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='capacity',
        ),
        migrations.RemoveField(
            model_name='warehouse',
            name='location',
        ),
        migrations.AddField(
            model_name='addware',
            name='exported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addware',
            name='imported',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='addware',
            name='order_received',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='addware',
            name='warehouse_from',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='importwares.warehouse'),
        ),
        migrations.AlterField(
            model_name='addware',
            name='description',
            field=models.CharField(max_length=700),
        ),
        migrations.AlterField(
            model_name='addware',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AlterField(
            model_name='addware',
            name='warehouse',
            field=models.CharField(max_length=100),
        ),
        migrations.DeleteModel(
            name='WareDescriptionReport',
        ),
        migrations.DeleteModel(
            name='WareIdReport',
        ),
        migrations.DeleteModel(
            name='WareImportQuantityReport',
        ),
        migrations.DeleteModel(
            name='WareNameReport',
        ),
        migrations.DeleteModel(
            name='WarePriceReport',
        ),
        migrations.DeleteModel(
            name='WareWarehouseReport',
        ),
        migrations.AddField(
            model_name='addware',
            name='warehouse_loc',
            field=models.ManyToManyField(to='importwares.warehouselocation'),
        ),
    ]