# Generated by Django 3.2.7 on 2021-10-20 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Train',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Train_id', models.IntegerField(max_length=30, null=True)),
                ('Train_name', models.CharField(max_length=30, null=True)),
                ('Source_id', models.IntegerField(max_length=30, null=True)),
                ('Destination_id', models.IntegerField(max_length=30, null=True)),
            ],
        ),
    ]