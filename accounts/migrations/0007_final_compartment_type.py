# Generated by Django 3.2.7 on 2021-10-23 10:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_final_phone_no'),
    ]

    operations = [
        migrations.AddField(
            model_name='final',
            name='Compartment_type',
            field=models.CharField(choices=[('Firstclass', '1A'), ('AC2tier class', 'AC2tier class'), ('AC 3tier class', 'AC 3tier class'), ('Sleeper class', 'Sleeper class'), ('Second class', 'Second class'), ('General class', 'General class')], max_length=30, null=True),
        ),
    ]
