# Generated by Django 4.1.7 on 2023-04-02 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospitalapp', '0002_rename_email_address_doctor_emailaddress_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='mobile',
            field=models.CharField(max_length=20),
        ),
    ]
