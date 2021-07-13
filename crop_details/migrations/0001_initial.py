# Generated by Django 3.2.4 on 2021-07-13 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product_Variety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('variety', models.CharField(max_length=200)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Crops',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('commodity', models.CharField(max_length=100)),
                ('image', models.ImageField(default='', upload_to='')),
                ('unit', models.CharField(choices=[('ExtBag', 'Ext Bag'), ('MedBunch', 'Med Bunch'), ('LgBox', 'Lg Box'), ('Bag', 'Bag'), ('SmBasket', 'Sm Basket'), ('net', 'net'), ('Dozen', 'Dozen'), ('crate', 'crate')], max_length=20)),
                ('volume_in_kgs', models.PositiveIntegerField()),
                ('values_in_ksh', models.FloatField(blank=True, default=0.0, null=True)),
                ('date', models.TextField(blank=True, null=True)),
                ('slug', models.SlugField()),
                ('product_variety', models.ManyToManyField(related_name='produce_variety', to='crop_details.Product_Variety')),
            ],
        ),
        migrations.CreateModel(
            name='Commodity_Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('commodity', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='crop_details.crops')),
            ],
        ),
    ]
