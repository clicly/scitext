# Generated by Django 4.1.7 on 2023-02-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_alter_booking_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='cpf',
            field=models.CharField(max_length=15, unique=True, verbose_name='CPF by responsable person'),
        ),
    ]
