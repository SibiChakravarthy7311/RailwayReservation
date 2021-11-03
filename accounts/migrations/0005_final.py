# Generated by Django 3.2.7 on 2021-10-23 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20211021_0538'),
    ]

    operations = [
        migrations.CreateModel(
            name='Final',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=40, null=True)),
                ('E_mail', models.CharField(max_length=40, null=True)),
                ('Age', models.IntegerField(null=True)),
                ('Gender', models.CharField(max_length=30, null=True)),
                ('train_name', models.CharField(max_length=30, null=True)),
                ('train_id', models.IntegerField(null=True)),
                ('no_of_booked_seats', models.IntegerField(null=True)),
                ('Source', models.CharField(max_length=30, null=True)),
                ('Destination', models.CharField(max_length=30, null=True)),
                ('Departure_time', models.CharField(max_length=30, null=True)),
                ('Arrival_time', models.CharField(max_length=30, null=True)),
                ('Fare', models.IntegerField(null=True)),
                ('PNR_no', models.IntegerField(null=True)),
                ('Status', models.CharField(max_length=40, null=True)),
            ],
        ),
    ]