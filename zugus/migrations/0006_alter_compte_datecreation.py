# Generated by Django 4.2.5 on 2023-10-16 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zugus', '0005_alter_device_is_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compte',
            name='dateCreation',
            field=models.DateField(auto_now_add=True, default=''),
            preserve_default=False,
        ),
    ]